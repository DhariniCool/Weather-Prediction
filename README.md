# Weather-Prediction

Django application to predict temperature for a given latitude and longitude. Its accepts one or more weather services as input. It could be noaa, weatherdotcom or accuweather and returns the average temperature for this location in json format.

The input latitude and longitude are validated using googlemaps. This application also takes zipcode of a location as input and it is converted to latitude and longitude using googlemaps for weather prediction.

