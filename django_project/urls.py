from django.conf.urls import include, url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ctracker/', include('ctracker.urls')),
    url(r'^tutorials/', include('tutorials.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
