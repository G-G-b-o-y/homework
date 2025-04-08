from django.contrib import admin
from . import models

admin.site.register(models.BoardAuthor)
admin.site.register(models.WeatherBoard)
admin.site.register(models.Location)