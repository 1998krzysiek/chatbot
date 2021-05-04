from django.conf.urls import url
from django.contrib import admin

from uploads.core import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    url('', views.home, name='home'),
    url('bosak/', views.bosak, name='bosak'),
    url('biedron/', views.biedron, name='biedron'),
    url('duda/', views.duda, name='duda'),
    url('holownia/', views.holownia, name='holownia'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]
