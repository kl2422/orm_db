from django.shortcuts import render
from .models import *
from django.views.generic.base import View, TemplateView
from django.http.response import HttpResponse

# Create your views here.

from django.http.request import QueryDict
class UserView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Hello Post World")

    def put(self, request, *args, **kwargs):
        # 格式化参数
        params = str(request.body, encoding="utf-8")
        q = QueryDict(params)
        return HttpResponse("Hello Put World")


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userName'] = 'Tonygogo'
        return context


from django.views.generic.list import ListView
class UserListView(ListView):

    model = UserInfo # 指定模型类
    # 指定返回模板名称，默认是当前app下的模型名小写.htmlusers/userinfo_list.html
    template_name = "user_list.html"


from django.views.generic.detail import DetailView
class UserDetailView(DetailView):
    model = UserInfo # 指定模型类
    # 指定返回模板名称，默认是<app_label>/<model_name><template_name_suffix>.html
    template_name = "user_detail.html"


def test(request):
    return HttpResponse("测试Redirect URL")

from django.views.generic.base import RedirectView
class RedirectTestView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'users:test' # 反向查找的地址

    def get_redirect_url(self, *args, **kwargs):
        # 业务逻辑
        return super().get_redirect_url(*args, **kwargs)


def set_session(request):
    request.session['test'] = '中国'
    return HttpResponse("设置session")


def get_session(request):
    value = request.session['test']
    return HttpResponse("获取session % s" % value)




