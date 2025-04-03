from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import ModelPost, Weather_data
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.template import loader
import datetime
import os
# Create your views here.

def get_sun(request):
    for date in Weather_data.get_sun_time():
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
        'loc_name_list':[
                {
                        "loc_eng": "Central",
                        "loc_chinese": "中西區"
                },
                {
                        "loc_eng": "EasternDistrict",
                        "loc_chinese": "東區"
                },
                {
                        "loc_eng": "IslandsDistrict",
                        "loc_chinese": "離島區"
                },
                {
                        "loc_eng": "KowloonCityDistrict",
                        "loc_chinese": "九龍城區"
                },
                {
                        "loc_eng": "KwunTongDistrict",
                        "loc_chinese": "觀塘區"
                },
                {
                        "loc_eng": "North",
                        "loc_chinese": "北區"
                },
                {
                        "loc_eng": "SaiKung",
                        "loc_chinese": "西貢區"
                },
                {
                        "loc_eng": "ShamShuiPoDistrict",
                        "loc_chinese": "深水埗區"
                },
                {
                        "loc_eng": "ShaTin",
                        "loc_chinese": "沙田區"
                },
                {
                        "loc_eng": "TaiPo",
                        "loc_chinese": "大埔區"
                },
                {
                        "loc_eng": "TsuenWanDistrict",
                        "loc_chinese": "荃灣區"
                },
                {
                        "loc_eng": "TuenMunDistrict",
                        "loc_chinese": "屯門區"
                },
                {
                        "loc_eng": "wanchai",
                        "loc_chinese": "灣仔區"
                },
                {
                        "loc_eng": "WongTaiSin",
                        "loc_chinese": "黃大仙區"
                },
                {
                        "loc_eng": "YauTsimMongDistrict",
                        "loc_chinese": "油尖旺區"
                },
                {
                        "loc_eng": "YuenLongDistrict",
                        "loc_chinese": "元朗區"
                }
        ]}
  return HttpResponse(template.render(context, request))



class ViewModelPost(ListView):
        queryset = ModelPost.objects.all()
        template_name = 'list.html'

class CreateModelPost(LoginRequiredMixin, CreateView):
        login_url = '/login/'
        model = ModelPost
        fields = '__all__'
        template_name = 'create_ModelPost_form.html'

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('list'))
                
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

class DeleteModelPost(DeleteView):
        model = ModelPost
        template_name = 'delete_ModelPost_form.html'

        def get_success_url(self):
                return reverse('list')


                