from django.http import HttpResponse

import logging
import json
import requests

def index(request):
  return HttpResponse("Hello, world" )

def accuweather(lat, lon):

  # URL to connect to accuweather api
  url = 'http://127.0.0.1:5000/accuweather'

  # Parameters for get request
  params = {'latitude':lat, 'longitute':lon}

# !!! Important !!!
# This part is commented because the flask server api does not work for accuweather. So, I am just returning a constant value here.
#  r = requests.get(url=url, params=params)
#  data = r.json()
#  return data

  return 50

def noaa(lat, lon):

  # URL to connect to noaa api.
  url = 'http://127.0.0.1:5000/noaa'

  # Form comma separated values of latitude and longitude to be supplied to get request.
  latlon = str(lat) + ',' + str(lon)
  params = {'latlon':latlon}

  # Submit the gett request and fetch the response
  r = requests.get(url=url, params=params)
  response = r.json()

  # Extract temperature for the response
  temp = response['today']['current']['fahrenheit']

  return temp

def weatherdotcom(lat, lon):

  # URL to connect to weatherdotcom
  url = 'http://127.0.0.1:5000/weatherdotcom'

  data = {"lat":lat,"lon":lon}

  # Submit the post request and extract the response.
  r = requests.post(url=url,json=data)
  response = r.json()

  # Extract temperature from the response. Temperature is within the response dictionary.
  temp = response['query']['results']['channel']['condition']['temp']
  
  return temp

def weather1(request, lat, lon, svc1):

  # Validate if the input latitude and longitude are valid.
  if ( validate_latlon( lat, lon ) ):

    # Fetch the temperature and form the response message.
    temp1 = fetch_temp( lat, lon, svc1 )
    msg = {'average_temperature':temp1}

  else:
    msg = {'result':'Invalid latitute/longitude'}

  output = json.dumps( msg )

  return HttpResponse( output )

def weather2(request, lat, lon, svc1, svc2):

  if ( validate_latlon( lat, lon ) ):

    # Store extracted temperature from different weather services.
    temp = []

    # Fetch temperature for each service.
    temp.append( fetch_temp( lat, lon, svc1 ) )
    temp.append( fetch_temp( lat, lon, svc2 ) )

    # Calculate average temperature
    avg_temp = sum(temp) / len(temp)

    msg = {'average_temperature':avg_temp}
  
  else:
    msg = {'result':'Invalid latitute/longitude'}

  output = json.dumps( msg )

  return HttpResponse( output )

def weather3(request, lat, lon, svc1, svc2, svc3):

  # Validate the input latitude and longitude
  if ( validate_latlon( lat, lon ) ):

    # Store the temperature from each weather service in a list.
    temp = []
    temp.append( fetch_temp( lat, lon, svc1 ) )
    temp.append( fetch_temp( lat, lon, svc2 ) )
    temp.append( fetch_temp( lat, lon, svc3 ) )

    # Calculate average temperature.
    avg_temp = sum(temp) / len(temp)

    msg = {'average_temperature':avg_temp}  

  else:  
    msg = {'result':'Invalid latitute/longitude'}
    
  output = json.dumps( msg )
  return HttpResponse( output )

def fetch_temp( lat, lon, svc ):

  lat = float(lat)
  lon = float(lon)

  # Based on the weather service, call approriate method that sends get request to the service.
  if svc == 'noaa':
    temp = noaa( lat, lon )
  elif svc == 'accuweather':
    temp = accuweather( lat, lon )
  elif svc == 'weatherdotcom':
    temp = weatherdotcom( lat, lon )

  return int(temp)

def validate( request, lat, lon ):

  # URL to connect to google maps api.
  url = "https://maps.googleapis.com/maps/api/geocode/json"

  # Pack latitude and longiture as parameters.
  latlon = lat + ',' + lon

  # Generate api key for googlemaps api.
  api_key = "AIzaSyA04-mA1PjLt4cT76B4cBvlsaxPYZ7PgWc"

  params_maps = {'latlng' : latlon, 'key' : api_key}

  # Submit get request.
  r = requests.get(url=url,params=params_maps)
  data = r.json()

  # Return the status from googlemaps. If the status is 'OK', it indicates the latitude and longitude pair is valid.
  return HttpResponse( data['status'] )

def validate_latlon(lat, lon):

  # URL to connect to googlemaps api.
  url = "https://maps.googleapis.com/maps/api/geocode/json"

  # Parameters for the request.
  latlon = lat + ',' + lon

  # API key generated to connect to googlemaps api.
  api_key = "AIzaSyA04-mA1PjLt4cT76B4cBvlsaxPYZ7PgWc"

  params_maps = {'latlng' : latlon, 'key' : api_key}

  # Submit the get request.
  r = requests.get(url=url,params=params_maps)
  data = r.json()

  # If the status is 'OK', it indicates that the latitude and longitude pair is valid.
  if data['status'] == 'OK':
    return True
  else:
    return False

def fetch_latlon( request, zipcode ):

# URL to connect to googlemaps api.
  url = "https://maps.googleapis.com/maps/api/geocode/json"

  # API key generated to connect to googlemaps api.
  api_key = "AIzaSyA04-mA1PjLt4cT76B4cBvlsaxPYZ7PgWc"

  params_maps = {'address' : zipcode, 'key' : api_key}

  # Submit the get request.
  r = requests.get(url=url,params=params_maps)

  data = r.json()

  lat = data['results'][0]['geometry']['location']['lat']
  lng = data['results'][0]['geometry']['location']['lng']

  msg = {'latitude':lat, 'longitude':lng}
  output = json.dumps( msg )

  return HttpResponse( output )

def fetch_lat_lon( zipcode ):

# URL to connect to googlemaps api.
  url = "https://maps.googleapis.com/maps/api/geocode/json"

  # API key generated to connect to googlemaps api.
  api_key = "AIzaSyA04-mA1PjLt4cT76B4cBvlsaxPYZ7PgWc"

  params_maps = {'address' : zipcode, 'key' : api_key}

  # Submit the get request.
  r = requests.get(url=url,params=params_maps)

  data = r.json()

  lat = data['results'][0]['geometry']['lat']['lng']
  lng = data['results'][0]['geometry']['lat']['lng']

  return lat, lng

def weather_zip1(request, zip, svc1):

  lat, lon = fetch_lat_lon( zip )

  # Validate if the input latitude and longitude are valid.
  if ( validate_latlon( lat, lon ) ):

   # Fetch the temperature and form the response message.
    temp1 = fetch_temp( lat, lon, svc1 )
    msg = {'average_temperature':temp1}

  else:
    msg = {'result':'Invalid latitute/longitude'}

  output = json.dumps( msg )

  return HttpResponse( output )

def weather_zip2(request, zip, svc1, svc2):

  lat, lon = fetch_lat_lon( zip )

  if ( validate_latlon( lat, lon ) ):

    # Store extracted temperature from different weather services.
    temp = []

    # Fetch temperature for each service.
    temp.append( fetch_temp( lat, lon, svc1 ) )
    temp.append( fetch_temp( lat, lon, svc2 ) )

    # Calculate average temperature
    avg_temp = sum(temp) / len(temp)

    msg = {'average_temperature':avg_temp}

  else:
    msg = {'result':'Invalid latitute/longitude'}

  output = json.dumps( msg )

  return HttpResponse( output )

def weather_zip3(request, zip, svc1, svc2, svc3):

  lat, lon = fetch_lat_lon( zip )

  # Validate the input latitude and longitude
  if ( validate_latlon( lat, lon ) ):

    # Store the temperature from each weather service in a list.
    temp = []
    temp.append( fetch_temp( lat, lon, svc1 ) )
    temp.append( fetch_temp( lat, lon, svc2 ) )
    temp.append( fetch_temp( lat, lon, svc3 ) )

    # Calculate average temperature.
    avg_temp = sum(temp) / len(temp)

    msg = {'average_temperature':avg_temp}

  else:
    msg = {'result':'Invalid latitute/longitude'}

  output = json.dumps( msg )

  return HttpResponse( output )
