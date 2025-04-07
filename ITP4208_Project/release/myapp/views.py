from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
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
                # reuturn all days
                return JsonResponse(date, safe=False)

def get_server_datetime(request):
        datetime_obj = datetime.datetime.today()
        time_dict = {
        "date":datetime_obj.strftime('%Y-%m-%d'),
        "time":datetime_obj.strftime('%H:%M'),
        "timestamp":int(datetime_obj.timestamp()*1000),
        }
        return JsonResponse(time_dict)

# get airplane data 
# bug
def airplane_information(request, date, way, *args):
        if way=="arrival":
               arrival="true"
        elif way=="departure":
               arrival="false"
        else :
               return HttpResponse(f"error params: {way}; only accept 'arrival' or 'departure'")
        result = Airplane.get_airplanes(date=date, arrival=arrival)
        return JsonResponse(result, safe=False)

def home_view(request):
        template = loader.get_template('home.html')
        context = loaction.get_weather_data()
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
        

class CreatWeatherBoard(CreateView):
        model = WeatherBoard
        fields = '__all__'
        template_name = 'create_weather_board.html'

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('createBoard'))

class DeleteWeatherBoard(DeleteView):
        model = WeatherBoard
        template_name = 'delete_weather_board.html'

        def get_success_url(self):
                return reverse('deleteBoard')

def weather_detail_view(request, district):
        loc_name_list = loaction.get_weather_data()["loc_name_list"]
        weather_data = next(item for item in loc_name_list if item["loc_eng"].lower() == district.lower())
        context = {
                "weather": {
                "district": weather_data["loc_chinese"],
                "temperature": weather_data["temperature"],
                "humidity": weather_data["humidity"],
                "wind_speed": weather_data["wind"],
                "condition": weather_data["condition"],
                "icon": f"images/{weather_data['condition']}.png",
                "description": f"{weather_data['condition']} weather with {weather_data['wind']} km/h winds"
                }
        }
        return render(request, 'weather_detail.html', context)

                