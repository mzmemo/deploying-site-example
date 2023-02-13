from django.conf.urls import url
from basic_app import views


urlpatterns = [
    url(r'^relative/$', views.relative, name='relativepage'),
    url(r'^other/$', views.other, name='other'),
]