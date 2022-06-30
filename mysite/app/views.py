from django.http import HttpResponse
from django.shortcuts import render
import requests
from mysite.settings_specific import OWM_API_KEY
from app.models import CitiesModel
from app.forms import CitiesForm

# Create your views here.
def home(request):
    
    cities = CitiesModel.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+ OWM_API_KEY
   
    weather_data = []

    if request.method =='POST':
        form = CitiesForm(request.POST)
        form.save()
        for city in cities:
            city_weather = requests.get(url.format(city)).json()
            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }
            
            weather_data.append(weather)
    
    form = CitiesForm()

    context = {
        'form':form,
        'weather_data' : weather_data
    }

    return render(request, 'home.html', context)


