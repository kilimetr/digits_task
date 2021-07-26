from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json



# Create your views here.
def index(request):
    url = "http://api.weatherapi.com/v1/forecast.json?key=361f4a39a7cb4ab892d131558211807&q={}&days={}"

    # vzít z modelu
    # country = Weather_Update.objects.all()[0]
    # date    = Weather_Update.date

    country = "UK"
    date = "2021-07-06"

    country = str(country)
    print(date)

    if country == "CZ":
        city = "Prague"

    elif country == "SK":
        city = "Bratislava"

    elif country == "UK":
        city = "London"

    days = 3

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

    context = {"weather": weather}

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


    return render(request, "weather_forecast/index.html", context)




def jresp_result(request, date, country_code):
    json_dict = {
        "date": date,
        "country_code": country_code
    }

    print(json_dict)

    return JsonResponse(json_dict)


