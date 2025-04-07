import requests
import time
import datetime

datetime_obj = datetime.datetime.today()
{
"date":datetime_obj.strftime('%Y-%m-%d'),
"time":datetime_obj.strftime('%H:%M'),
"timestamp":int(datetime_obj.timestamp()*1000),
}


params = {
            "date":datetime_obj.strftime('%Y-%m-%d'),
            "lang":"en",
            "cargo":"false",
            "arrival":"false"
        }
response = requests.get("https://www.hongkongairport.com/flightinfo-rest/rest/flights/past", params=params)
for i in response.json():
    if params["date"] == i["date"]:
        for x in i["list"]:
                print(x)