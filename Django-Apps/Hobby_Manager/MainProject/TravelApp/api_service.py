import requests


DARK_SKY_KEY = 'dde7f2968ecb35dfafee87c93912caf0'
DARK_SKY_KEY_2 = '0d1d9e6ec4c3bce46a0dbbef84283387'


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


def get_current_weather(lat, lon):
    base_url = f'https://api.darksky.net/forecast/{DARK_SKY_KEY_2}/{lat},{lon}'
    params = {
        'exclude': ['minutely',
                    'hourly',
                    'daily',
                    'alerts',
                    'flags']
    }
    unformatted_current_weather = requests.get(base_url, params).json()
    current_weather = unformatted_current_weather['currently']
    return current_weather
