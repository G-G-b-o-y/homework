import requests
import time
import datetime

datetime_obj = datetime.datetime.today()
print({
        "date":datetime_obj.strftime('%Y-%m-%d'),
        "time":datetime_obj.strftime('%H:%M'),
        "timestamp":int(datetime_obj.timestamp()*1000),
        })