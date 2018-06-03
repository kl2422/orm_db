from django.urls import path
from . import views
from . import models

app_name = 'employee'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('test_rs/', views.test1, name='test_rs'),
    path('rs/<int:id>', views.rs, name='rs'),
    # path('dept/', views.list_dept, name='list_dept'),
    # path('emps/', views.list_emps, name='list_emps'),
    path('dept/', views.list, {'model': models.Dept}, name='list_dept'),
    path('emps/', views.list, {'model': models.Emp}, name='list_emps'),

    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('read_cookie/', views.read_cookie, name='read_cookie'),
    path('read_some_cookie/<str:key>/<str:salt>/', views.read_some_cookie, name='read_some_cookie'),
    path('delete_cookie/', views.delete_cookie, name='delete_cookie'),


    path('http_method/', views.http_method, name='http_method'),
    path('http_get_method/', views.http_get_method, name='http_get_method'),
    path('http_post_method/', views.http_post_method, name='http_post_method'),
    path('http_put_method/', views.http_put_method, name='http_put_method'),
    path('http_delete_method/', views.http_delete_method, name='http_delete_method'),
    path('http_safe_method/', views.http_safe_method, name='http_safe_method'),

    path('ajax/', views.ajax, name='ajax'),
]
