from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core.exceptions import PermissionDenied

# Create your views here.


def add(request):
    raise Http404
    return HttpResponse("添加学生信息！")


def update(request, id):
    raise Exception
    return HttpResponse("修改学生信息！%d" % id)


def delete(request, id):
    raise PermissionDenied
    return HttpResponse("删除学生信息！%d" % id)

def test(request):
    return render(request, "test.html")

import json
def do_jsonp(request):
    callback = request.GET.get('callback')
    result = json.dumps({'id': 123, 'name': 'Jack'})
    print(type(result))
    if callback:
        c = callback + "(" + result + ")"
    else:
        c = result
    return HttpResponse(c)


def children(request):
    return render(request, "children.html", {'blog_entries':['内容一','内容二','内容三',]})