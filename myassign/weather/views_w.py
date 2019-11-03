#path('weather/<float:lat>/<float:lon>/accuweather/', views.accuweather ),
#path('weather/<float:lat>/<float:lon>/noaa/', views.noaa ),
#path('weather/<float:lat>/<float:lon>/weatherdotcom/', views.weatherdotcom )

from django.http import HttpResponse

import json
import requests

def index(request):
  return HttpResponse("Hello, world" )

def test( request ):

  lat = request.GET['lat']
#  lon = request.GET['lon']
 
#  msg = str(lat) + ':' + str(lon)

  return HttpResponse(str(lat))

def weather( request, lat ):
  response = "You are looking at %s"
  return HttpResponse (response % lat )

def accuweather(request, lat, lon):
  return HttpResponse("Hello")

def noaa(lat, lon):
  url = 'http://127.0.0.1:5000/noaa'

    # Form comma separated values of latitude and longitude to be supplied to get request.
  latlon = str(lat) + ',' + str(lon)
  params = {'latlon':latlon}

  r = requests.get(url=url, params=params)
  response = r.json()

  temp = response['today']['current']['fahrenheit']

def noaa(request, lat, lon):

  url = 'http://127.0.0.1:5000/noaa'

  # Form comma separated values of latitude and longitude to be supplied to get request.
  latlon = str(lat) + ',' + str(lon)
  params = {'latlon':latlon}

  r = requests.get(url=url, params=params)
  response = r.json()

  temp = response['today']['current']['fahrenheit']

  return HttpResponse( temp )

def weatherdotcom(request, lat, lon):

  url = 'http://127.0.0.1:5000/weatherdotcom'

  data = {"lat":lat,"lon":lon}
  r = requests.post(url=url,json=data)

  response = r.json()

  # Extract temperature from the response. Temperature is within the response dictionary.
  temp = response['query']['results']['channel']['condition']['temp']
  #temp = 'jey'
  return HttpResponse( temp )
