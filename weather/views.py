from django.shortcuts import render

import requests
# Create your views here.

def index(request):
    if request.method == "POST" or request.method == "GET":
        city = request.POST.get('city')
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4585824b496878ca2b0388497ec252a5"
        
        data = requests.get(url.format(city)).json()
        print(data)

        context = {
            'city' : city,
            'temperature' : data['main']['temp'],
            'description' : data['weather'][0]['description'],
            'icon' : data['weather'][0]['icon'],
            'humidity' : data['main']['humidity'],
        
        }

        return render(request, "index.html", context)
    
    # return render(request, "index.html", context)
    