from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import ModelPost, YearSunUpDown, WeatherData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.template import loader
import datetime
import random
import os
# Create your views here.

def get_sun(request):
    for date in YearSunUpDown.get_sun_time():
        if datetime.datetime.today().strftime('%Y-%m-%d') == date[0]:
                return JsonResponse(date, safe=False)

def get_server_datetime(request):
        datetime_obj = datetime.datetime.today()
        time_dict = {
        "date":datetime_obj.strftime('%Y-%m-%d'),
        "time":datetime_obj.strftime('%H:%M'),
        "timestamp":int(datetime_obj.timestamp()*1000),
        }
        return JsonResponse(time_dict)

def home_view(request):
  template = loader.get_template('home.html')
  context = {
        "loc_name_list": [
                {
                "loc_eng": "Central",
                "loc_chinese": "中西區",
                "temperature": 12,
                "wind": 3,
                "direction": "East",
                "humidity": 79,
                "rainfall": 0.5
                },
                {
                "loc_eng": "EasternDistrict",
                "loc_chinese": "東區",
                "temperature": 14,
                "wind": 5,
                "direction": "North",
                "humidity": 75,
                "rainfall": 0.0
                },
                {
                "loc_eng": "IslandsDistrict",
                "loc_chinese": "離島區",
                "temperature": 16,
                "wind": 7,
                "direction": "South",
                "humidity": 80,
                "rainfall": 1.2
                },
                {
                "loc_eng": "KowloonCityDistrict",
                "loc_chinese": "九龍城區",
                "temperature": 15,
                "wind": 4,
                "direction": "West",
                "humidity": 78,
                "rainfall": 0.8
                },
                {
                "loc_eng": "KwunTongDistrict",
                "loc_chinese": "觀塘區",
                "temperature": 14,
                "wind": 6,
                "direction": "East",
                "humidity": 77,
                "rainfall": 0.3
                },
                {
                "loc_eng": "North",
                "loc_chinese": "北區",
                "temperature": 13,
                "wind": 4,
                "direction": "North",
                "humidity": 76,
                "rainfall": 0.0
                },
                {
                "loc_eng": "SaiKung",
                "loc_chinese": "西貢區",
                "temperature": 15,
                "wind": 5,
                "direction": "South",
                "humidity": 79,
                "rainfall": 2.1
                },
                {
                "loc_eng": "ShamShuiPoDistrict",
                "loc_chinese": "深水埗區",
                "temperature": 16,
                "wind": 3,
                "direction": "West",
                "humidity": 75,
                "rainfall": 0.7
                },
                {
                "loc_eng": "ShaTin",
                "loc_chinese": "沙田區",
                "temperature": 14,
                "wind": 4,
                "direction": "East",
                "humidity": 77,
                "rainfall": 0.9
                },
                {
                "loc_eng": "TaiPo",
                "loc_chinese": "大埔區",
                "temperature": 13,
                "wind": 5,
                "direction": "North",
                "humidity": 78,
                "rainfall": 1.5
                },
                {
                "loc_eng": "TsuenWanDistrict",
                "loc_chinese": "荃灣區",
                "temperature": 15,
                "wind": 6,
                "direction": "South",
                "humidity": 76,
                "rainfall": 0.4
                },
                {
                "loc_eng": "TuenMunDistrict",
                "loc_chinese": "屯門區",
                "temperature": 14,
                "wind": 7,
                "direction": "West",
                "humidity": 79,
                "rainfall": 0.6
                },
                {
                "loc_eng": "wanchai",
                "loc_chinese": "灣仔區",
                "temperature": 16,
                "wind": 4,
                "direction": "East",
                "humidity": 75,
                "rainfall": 0.2
                },
                {
                "loc_eng": "WongTaiSin",
                "loc_chinese": "黃大仙區",
                "temperature": 15,
                "wind": 5,
                "direction": "North",
                "humidity": 77,
                "rainfall": 1.0
                },
                {
                "loc_eng": "YauTsimMongDistrict",
                "loc_chinese": "油尖旺區",
                "temperature": 16,
                "wind": 6,
                "direction": "South",
                "humidity": 78,
                "rainfall": 0.1
                },
                {
                "loc_eng": "YuenLongDistrict",
                "loc_chinese": "元朗區",
                "temperature": 14,
                "wind": 4,
                "direction": "West",
                "humidity": 76,
                "rainfall": 0.0
                }
        ]
        }
  return HttpResponse(template.render(context, request))

class ViewWeatherData(ListView):
        queryset = WeatherData.objects.all()
        template_name = 'days_forecast.html'

class CreateWeatherData(CreateView):
        model = WeatherData
        fields = '__all__'
        template_name = 'create_days_forecast.html'

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('9dayforecast'))
        
class DeleteWeatherData(DeleteView):
        model = WeatherData
        template_name = 'delete_days_forecast.html'

        def get_success_url(self):
                return reverse('days_forecast')
        
                
class UpdateModelPost(UpdateView):
        model = ModelPost
        fields = ['title', 'author', 'content']
        template_name = 'update_ModelPost_form.html'

        def get_object(self, queryset=None):
                id = self.kwargs['id']
                return self.model.objects.get(id=id)

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('list'))



                