from django.shortcuts import render
from requests import get

from .models import City

api_key = "e5fee864aec066e146ee446fb6e64407"


def index(request, *args, **kwargs):

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        r = get(url).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': weather_data}

    return render(request, 'weather/weather.html', context)
