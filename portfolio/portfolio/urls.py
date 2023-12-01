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
from django.urls import include, re_path
from django.contrib import admin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from portfolioapp.views import PBlog, PBlog_List, PBlog_Create, register
# from django.contrib.auth.views import login, logout
urlpatterns = [

    re_path(r'^home$', TemplateView.as_view(template_name="home.html"), name='home'),
    re_path(r'^resume$', TemplateView.as_view(template_name="resume.html"), name='resume'),
    re_path(r'^register/$', register, name="register"),
    # re_path(r'^logout/', logout, {'next_page': '/home'}, name="logout"),
    # re_path(r'^accounts/login/', login, name="login"),
    re_path(r'^work$', TemplateView.as_view(template_name="work.html"), name='work'),
    re_path(r'^pblog/(?P<pk>\d+)/$', PBlog.as_view(), name="blog_post"),
    re_path(r'^blog_post_create/$', PBlog_Create.as_view(), name="blog_create"),
    # url(r'^pblog/(?P<pk>\d+)/$', PBlog.as_view(), name="blog_post"),
    # url(r'^blog_post/(?P<pk>\d+)/$', blog_template, name="blog_post"),
    # url(r'^blog_post_create/$', PBlog_Create, name="blog_create"),


    # re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('home')),
    name='redirect_home'),

]
