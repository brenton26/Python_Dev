import requests
from datetime import datetime

# API keys
DARK_SKY_KEY = 'dde7f2968ecb35dfafee87c93912caf0'
DARK_SKY_KEY_2 = '0d1d9e6ec4c3bce46a0dbbef84283387'
OPEN_CAGE_KEY = '08ad530eddbe462e82652a836cb2ec56'


# uses ip-api to get a user's latitude and longitude coordinates
def get_user_location():
    data = requests.get("http://ip-api.com/json").json()
    latitude = data['lat']
    longitude = data['lon']
    city = data['city']
    state = data['regionName']
    location = {
        'latitude': latitude,
        'longitude': longitude,
        'city': city,
        'state': state,
    }
    return location


# Uses the Dark Sky API by passing in a set of coordinates to find current weather of that location
# Dark Sky Free API is limited to 1000 calls/day, so if one key goes over the limit change to the other key
def get_current_weather(lat, lon):
    base_url = f'https://api.darksky.net/forecast/{DARK_SKY_KEY_2}/{lat},{lon}'
    params = {
        'exclude': ['minutely',
                    'hourly',
                    'alerts',
                    'flags']
    }
    raw_weather_data = requests.get(base_url, params).json()

    weather = {
        'temperature': raw_weather_data['currently']['temperature'],
        'apparentTemperature': raw_weather_data['currently']['apparentTemperature'],
        'icon': raw_weather_data['currently']['icon'],
        'summary': raw_weather_data['currently']['summary'],
        'cloudCover': raw_weather_data['currently']['cloudCover']*100,
        'humidity': raw_weather_data['currently']['humidity']*100,
        'visibility': raw_weather_data['currently']['visibility'],
        'windSpeed': raw_weather_data['currently']['windSpeed'],
        'week_summary': raw_weather_data['daily']['summary'],
        'week_icon': raw_weather_data['daily']['icon'],
        'day0_day_of_week': datetime.fromtimestamp(raw_weather_data['daily']['data'][0]['time']).strftime('%a').upper(),
        'day0_high_temp': raw_weather_data['daily']['data'][0]['temperatureHigh'],
        'day0_low_temp': raw_weather_data['daily']['data'][0]['temperatureLow'],
        'day0_icon': raw_weather_data['daily']['data'][0]['icon'],
        'day1_day_of_week': datetime.fromtimestamp(raw_weather_data['daily']['data'][1]['time']).strftime('%a').upper(),
        'day1_high_temp': raw_weather_data['daily']['data'][1]['temperatureHigh'],
        'day1_low_temp': raw_weather_data['daily']['data'][1]['temperatureLow'],
        'day1_icon': raw_weather_data['daily']['data'][1]['icon'],
        'day2_day_of_week': datetime.fromtimestamp(raw_weather_data['daily']['data'][2]['time']).strftime('%a').upper(),
        'day2_high_temp': raw_weather_data['daily']['data'][2]['temperatureHigh'],
        'day2_low_temp': raw_weather_data['daily']['data'][2]['temperatureLow'],
        'day2_icon': raw_weather_data['daily']['data'][2]['icon'],
        'day3_day_of_week': datetime.fromtimestamp(raw_weather_data['daily']['data'][3]['time']).strftime('%a').upper(),
        'day3_high_temp': raw_weather_data['daily']['data'][3]['temperatureHigh'],
        'day3_low_temp': raw_weather_data['daily']['data'][3]['temperatureLow'],
        'day3_icon': raw_weather_data['daily']['data'][3]['icon'],
        'day4_day_of_week': datetime.fromtimestamp(raw_weather_data['daily']['data'][4]['time']).strftime('%a').upper(),
        'day4_high_temp': raw_weather_data['daily']['data'][4]['temperatureHigh'],
        'day4_low_temp': raw_weather_data['daily']['data'][4]['temperatureLow'],
        'day4_icon': raw_weather_data['daily']['data'][4]['icon'],
        'day5_day_of_week': datetime.fromtimestamp(raw_weather_data['daily']['data'][5]['time']).strftime('%a').upper(),
        'day5_high_temp': raw_weather_data['daily']['data'][5]['temperatureHigh'],
        'day5_low_temp': raw_weather_data['daily']['data'][5]['temperatureLow'],
        'day5_icon': raw_weather_data['daily']['data'][5]['icon'],
        'day6_day_of_week': datetime.fromtimestamp(raw_weather_data['daily']['data'][6]['time']).strftime('%a').upper(),
        'day6_high_temp': raw_weather_data['daily']['data'][6]['temperatureHigh'],
        'day6_low_temp': raw_weather_data['daily']['data'][6]['temperatureLow'],
        'day6_icon': raw_weather_data['daily']['data'][6]['icon'],
    }
    print(weather)
    return weather


# Uses Open Cage GeoCoding API. Passes in a location string and the API returns that location's coordinates
def get_queried_location(query_string):
    url = 'https://api.opencagedata.com/geocode/v1/json/'
    params = {
        'key': OPEN_CAGE_KEY,
        'q': query_string,
        'limit': 1,
    }
    data = requests.get(url, params=params).json()
    latitude = data['results'][0]['geometry']['lat']
    longitude = data['results'][0]['geometry']['lng']
    city = data['results'][0]['components']
    city = city.get('city')
    if city is None:
        city = data['results'][0]['components']
        city = city.get('county', 'Somewhere')
    state = data['results'][0]['components']
    state = state.get('state')
    if state is None:
        state = data['results'][0]['components']
        state = state.get('country')
        if state is None:
            state = data['results'][0]['components']
            state = state.get('continent', 'Somewhere')
    location = {
        'latitude': latitude,
        'longitude': longitude,
        'city': city,
        'state': state,
    }
    return location

