from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db import transaction
from django.shortcuts import reverse

# Create your views here.
from employee.models import Dept, Emp, SaleGrade


@transaction.non_atomic_requests
# @transaction.atomic
def add(request):
    # with transaction.atomic():
    #     Dept.objects.create(dname='测试', loc='测试')
    #     raise Exception
    #     Dept.objects.create(dname='测试', loc='测试')
    Dept.objects.create(dname='测试', loc='测试')
    raise Exception
    Dept.objects.create(dname='测试', loc='测试')


def rs(request, id):
    return HttpResponse("跳到这里来了：%d"%id)


def test1(request):
    return HttpResponseRedirect(reverse('employee:rs', args=(123, )))


# 展示所有的部门信息
def list_dept(request):
    depts = Dept.objects.all()
    return render(request, "dept_list.html", {depts: depts})


# 展示所有员工信息
def list_emps(request):
    emps = Dept.objects.all()
    return render(request, "emp_list.html", {emps: emps})


def list(request, model):
    print(request.COOKIES)
    objs = model.objects.all()
    template_name = '%s_list.html' % model.__name__.lower()
    return render(request, template_name, {'items': objs})


# 设置cookie，如果有中文需要转码
def set_cookie(request):
    response = HttpResponse("测试设置Cookie")
    # 过期日期如果没有携带就是session cookie，默认domain是当前访问的域名，path默认是/
    t = request.GET.get('type')
    t = int(t)
    if t == 1:
        response.set_cookie("userId", "1234")
    elif t == 2: # max_age单位秒
        response.set_cookie("max_age", "1234", max_age=10)
    elif t == 3: # expire会覆盖max_age
        import datetime
        response.set_cookie("max_age_expire", "1234", max_age=10, expires=datetime.datetime(2018, 5, 28))
    elif t == 4:# 设置path, 只能在当前path下的访问路径才能看到
        response.set_cookie("max_age_path", "1234", max_age=60, path="/employee/read_cookie")
    elif t == 5:# 只能在当前或顶级域名下设置
        response.set_cookie("max_age_domain", "1234", max_age=60, domain="www.shsxt.com")
    elif t == 6:  # secure设置安全的cookie，只能在https请求中设置
        response.set_cookie("max_age_domain_secure", "1234", max_age=60, domain="www.shsxt.com", secure=True)
    elif t == 7:  # httponly设置不让js访问
        response.set_cookie("max_age_domain_httponly", "1234", max_age=60, httponly=True)
    else: # 设置加密的cookie
        response.set_signed_cookie("userName", "上海尚学堂".encode("utf-8"), "shsxt")
    return response



# 读取所有的
def read_cookie(request):
    cookies = request.COOKIES
    for k, v in cookies.items():
        print("cookie的key值：%s, value值：%s" % (k, v))
    return render(request, "cookie_read.html", {'cookies': cookies})

#读取某个cookie
def read_some_cookie(request, key, salt = ''):
    value = request.get_signed_cookie(key, salt=salt)
    return HttpResponse("获取到的cookie值：%s" % value)

def delete_cookie(request):
    response = HttpResponse("删除userId的cookie")
    response.delete_cookie("userId")
    return response


from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe

@require_http_methods(['GET', 'POST'])
def http_method(request):
    return HttpResponse("只接受GET和POST请求")

@require_GET
def http_get_method(request):
    return HttpResponse("只接受GET请求")

@require_POST
def http_post_method(request):
    return HttpResponse("只接受POST请求")

@require_http_methods(['PUT'])
def http_put_method(request):
    return HttpResponse("只接受PUT请求")

@require_http_methods(['DELETE'])
def http_delete_method(request):
    return HttpResponse("只接受DELETE请求")

@require_safe
def http_safe_method(request):
    return HttpResponse("只接受GET和HEADER请求")


import json
def ajax(request):
    print("是否是ajax请求：%s" % request.is_ajax())
    id = request.GET['id']
    content ={"code": 200, "message": "请求成功", "results": id}
    return HttpResponse(json.dumps(content), content_type="application/json")

