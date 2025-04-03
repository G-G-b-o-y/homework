"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path as url
from django.views.generic import TemplateView
from myapp.views import ViewModelPost, CreateModelPost, UpdateModelPost, DeleteModelPost, get_sun, home_view
from myapp.register import signup
from django.contrib.auth import views as auth_views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^login/?$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/?$', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    url(r'^signup/?$', signup, name='signup'),

    url(r'^weather/sun/?$', get_sun),
    
    url(r'^contact/$', TemplateView.as_view(template_name='danmutanchuang.html'), name='contact'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^list/$', ViewModelPost.as_view(), name='list'),
    url(r'^create/$', CreateModelPost.as_view(), name='create'),
    url(r'^update/(?P<id>\d)/$', UpdateModelPost.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d)/$', DeleteModelPost.as_view(), name='delete')
]


# SUM:https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=SRS&year=2025&rformat=json
# MOOB:https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=MRS&year=2025&rformat=json
