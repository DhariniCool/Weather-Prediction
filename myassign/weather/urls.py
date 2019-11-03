"""jd_weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('',views.index, name='index'),

    # URL that validates the input latitude and longitude.
    path('<str:lat>/<str:lon>/', views.validate ),

    # URL that converts zipcode to latitude and longitude
    path('<str:zipcode>/', views.fetch_latlon ),

    # URLS that supports latitude, longitude along with the services.
    path('<str:lat>/<str:lon>/<str:svc1>/', views.weather1 ),
    path('<str:lat>/<str:lon>/<str:svc1>/<str:svc2>/', views.weather2 ),
    path('<str:lat>/<str:lon>/<str:svc1>/<str:svc2>/<str:svc3>/', views.weather3 ),
    
    # URLs that supports zipcode as input
    path('<str:zip>/<str:svc1>/', views.weather_zip1 ),
    path('<str:zip>/<str:svc1>/<str:svc2>/', views.weather_zip2 ),
    path('<str:zip>/<str:svc1>/<str:svc2>/<str:svc3>/', views.weather_zip3 ),
]

