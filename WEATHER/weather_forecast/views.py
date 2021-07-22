from django.shortcuts import render
# from django.http import HttpResponse
import requests
from weather_forecast.models import Weather_Update
from weather_forecast.forms import Weather_Update_Form
import json



# Create your views here.
def index(request):
    url = "http://api.weatherapi.com/v1/forecast.json?key=361f4a39a7cb4ab892d131558211807&q={}&days={}"

    country = Weather_Update.objects.all()[0]
    date    = Weather_Update.date

    country = str(country)
    print(date)

    if country == "CZ":
        city = "Prague"

    elif country == "SK":
        city = "Bratislava"

    elif country == "UK":
        city = "London"

    days = 3

    form = Weather_Update_Form()

    response = requests.get(url.format(city, days))

    if response.status_code != 200:
        print("\n \n \n!!! SORRY, CRASHED !!!\n \n \n")

    response = requests.get(url.format(city, days)).json()

    weather = {
        "country": country,
        "city": response["location"]["name"],
        "date": response["forecast"]["forecastday"][0]["date"],
        "temp_av": response["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        }

    context = {"weather": weather, "form": form}

    if country == "CZ":
        city = "Prague"

    elif country == "SK":
        city = "Bratislava"

    elif country == "UK":
        city = "London"


    if context["weather"]["temp_av"] > 20:
        answer = "good"

    elif 10 <= context["weather"]["temp_av"] <= 20:
        answer = "soso"

    else:
        answer = "bad"

    final = {"forecast": answer}

    def answer_fun(request, answer):
        print(request.GET)
        return render(request, "weather_forecast/index.html", json.dumps(final))


    return render(request, "weather_forecast/index.html", context, answer_fun)

