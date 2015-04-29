from django.conf.urls import patterns, include, url
from MyViewApp import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include('MyTaskData.urls')),
    url(r'^admin/', include(admin.site.urls)),
     url(r'^myview/',views.myView),
)