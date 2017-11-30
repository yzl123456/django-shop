# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^/$',views.index,name='indexPage2'),
    url(r'^index/$',views.index,name='indexPage'),

 	url(r'^loginOut/$',views.loginOut,name='loginOut'),

    ]

