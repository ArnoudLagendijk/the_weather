from django.shortcuts import render
from requests import get

api_key = "e5fee864aec066e146ee446fb6e64407"


def index(request, *args, **kwargs):
    city = "Zoetermeer"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = get(url)
    print(r.text)
    return render(request, 'weather/weather.html')
