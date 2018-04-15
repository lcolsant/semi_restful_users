from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^users/new$', views.new_user),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<id>\d+)/show$', views.show),
    url(r'^users/(?P<id>\d+)/edit$', views.edit),
    url(r'^users/(?P<id>\d+)/delete$', views.destroy),
    url(r'^users/(?P<id>\d+)/update$', views.update),

]