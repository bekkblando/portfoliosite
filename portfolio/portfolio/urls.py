"""portfolio URL Configuration

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
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from portfolioapp.views import PBlog, PBlog_List, PBlog_Create, register
from django.contrib.auth.views import login, logout
urlpatterns = [

    url(r'^home$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^resume$', TemplateView.as_view(template_name="resume.html"), name='resume'),
    url(r'^register/$', register, name="register"),
    url(r'^logout/', logout, {'next_page': '/home'}, name="logout"),
    url(r'^accounts/login/', login, name="login"),
    url(r'^work$', TemplateView.as_view(template_name="work.html"), name='work'),
    url(r'^pblog/(?P<pk>\d+)/$', PBlog.as_view(), name="blog_post"),
    url(r'^blog_post_create/$', PBlog_Create.as_view(), name="blog_create"),
    # url(r'^pblog/(?P<pk>\d+)/$', PBlog.as_view(), name="blog_post"),
    # url(r'^blog_post/(?P<pk>\d+)/$', blog_template, name="blog_post"),
    # url(r'^blog_post_create/$', PBlog_Create, name="blog_create"),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('home')),
    name='redirect_home'),

]
