from django.urls import path
from . import views

app_name = 'users'
from .views import *
urlpatterns = [
    path('index/', UserView.as_view(), name='user_view'),
    path('home/', HomePageView.as_view(), name='home'),
    path('list/', UserListView.as_view(), name='user_list'),
    # path('detail/<slug:slug>/', UserDetailView.as_view(), name='user_detail'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('redirect/', RedirectTestView.as_view(), name='test-redirect'),
    path('test/', test, name='test'),
    path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),

    path('set_session/', set_session, name='set_session'),
    path('get_session/', get_session, name='get_session'),
]
