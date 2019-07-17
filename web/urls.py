from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^template/$', views.template, name='template'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
]