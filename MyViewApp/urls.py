from django.conf.urls import patterns, url
from MyViewApp import views

urlpatterns = patterns(
    '',
    url(r'^$',views.myPanel,name="myPanel"),
    url(r'^deleteme/(?P<id>\d+)/$',views.deleteme),
    url(r'^editme/(?P<id>\d+)/$', views.editme),
 url(r'^addData/$', views.addme),
)

