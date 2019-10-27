from django.urls import include, path, re_path
from django.conf.urls import url
from .views import *
app_name = 'app'


urlpatterns = [

    path('list/', view = list, name='list'),
    path('create/', view=create, name='create'),
    url('^detail/(?P<pk>[0-9]+)$', view=detail, name='detail'),
    re_path('^update/(?P<pk>[0-9]+)$', view=update, name='update'),
    re_path('^delete/(?P<pk>[0-9]+)$', view=delete, name='delete'),
    re_path('^comment_delete/(?P<pk>[0-9]+)$', view=comment_delete, name='comment_delete'),
    re_path('^comment_update/(?P<pk>[0-9]+)$', view=comment_update, name='comment_update'),



]