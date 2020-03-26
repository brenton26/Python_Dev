from django.shortcuts import render
from .api_service import *
import json


# Create your views here.
def home(request):
    return render(request, 'TravelApp/travel_home.html')


def weather(request):
    if request.method == 'POST':
        user_input = request.POST.get('weather-search-string', None)
        location = get_queried_location(user_input)
        lat = location['latitude']
        lon = location['longitude']
        city = location['city']
        state = location['state']
        current_weather = get_current_weather(lat, lon)
        context = {
            'weather': current_weather,
            'city': city,
            'state': state,
        }
        return render(request, 'TravelApp/travel_weather_default.html', context)
    else:
        location = get_user_location()
        lat = location['latitude']
        lon = location['longitude']
        city = location['city']
        state = location['state']
        current_weather = get_current_weather(lat, lon)
        context = {
            'weather': current_weather,
            'city': city,
            'state': state,
        }
        return render(request, 'TravelApp/travel_weather_default.html', context)




