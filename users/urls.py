from django.urls import include, path, re_path
from django.conf.urls import url
from .views import *
app_name = 'users'


urlpatterns = [

    path('register/', view = register, name='register'),
    path('login/', view=user_login, name='user_login'),
    path('logout/', view=user_logout, name='user_logout'),

]