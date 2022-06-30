from django.shortcuts import render
import requests
from mysite.settings_specific import OWM_API_KEY



# Create your views here.
def home(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+ OWM_API_KEY
    
    city = 'Paris'

    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {
        'weather' : weather
    }

    return render(request, 'home.html', context)