from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('add', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('test/', views.test, name='test'),
    path('do_jsonp/', views.do_jsonp, name='do_jsonp'),

    path('children/', views.children, name='children'),
]
