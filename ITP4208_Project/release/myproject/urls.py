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
from myapp.views import *
from myapp.register import signup
from django.contrib.auth import views as auth_views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^airportSite/$', TemplateView.as_view(template_name="airplane.html"), name='airplane'),
    url(r'^clock/$', TemplateView.as_view(template_name='clock.html'), name='contact'),
    url(r'^9dayforecast/$', ViewWeatherData.as_view(template_name='days_forecast.html'), name='days_forecast'),
    url(r'^createWeatherData/$', CreateWeatherData.as_view(template_name='create_days_forecast.html'), name='9dayforecast'),
    url(r'^deleteWeatherData/(?P<pk>\d{4}-\d{2}-\d{2})/$', DeleteWeatherData.as_view(), name='delete'),

    url(r'^createWeatherBoard/$', CreateWeatherBoard.as_view(template_name='create_weather_board.html'), name='createBoard'),
    # url(r'^deleteWeatherBoard/(?P<pk>\d)/$', DeleteWeatherBoard.as_view(), name='deleteBoard'),
    
    url(r'^weather/sun/?$', get_sun),
    url(r'^weather/clock/$', get_server_datetime),
    url(r'^airport/(\d{4}-\d{2}-\d{2})/(\b(arrival|departure)\b)$', airplane_information, name='airport'),

    url(r'^login/?$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/?$', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    url(r'^signup/?$', signup, name='signup'),
    
    url(r'^weather_detail/(?P<district>\w+)/$', weather_detail_view, name='weather_detail')
]


# SUM:https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=SRS&year=2025&rformat=json
# MOOB:https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=MRS&year=2025&rformat=json
