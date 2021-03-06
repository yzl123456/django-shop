"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from index.views import search
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^search/', include('haystack.urls')),
    url(r'^',include('registerLogin.urls',namespace='registerLogin')),
    url(r'^',include('usercenter.urls',namespace='usercenter')),
    url(r'^', include('goodslist.urls', namespace='goodslist')),
    url(r'^',include('index.urls',namespace='index')),
    url(r'^',include('detail.urls',namespace='detail')),
    url(r'^',include('cart.urls',namespace='cart')),
    url(r'^search/', search, name='search_view'),
    #url(r'^search/', viewSearch.MySearchView.as_view(), name='search_view'),
]
