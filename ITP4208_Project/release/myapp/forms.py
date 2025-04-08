from django import forms
from .models import WeatherBoard, Location

class WeatherBoardForm(forms.ModelForm):
    class Meta:
        model = WeatherBoard
        fields = ['user', 'locations']  # 确保包含 'locations'
        
    locations = forms.ModelMultipleChoiceField(
        queryset=Location.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # 使用复选框
        required=False
    )