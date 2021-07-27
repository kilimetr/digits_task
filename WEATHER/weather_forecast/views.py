from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
import datetime



# Create your views here.
def index(request):
    url = "http://api.weatherapi.com/v1/forecast.json?key=361f4a39a7cb4ab892d131558211807&q={}&days={}"

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
    date_separ = date.split("-")

    today_date       = datetime.date.today()
    today_date_year  = today_date.year # type int
    today_date_month = today_date.month
    today_date_day   = today_date.day


    date_separ = date.split("-") # year, day, month

    i = 0
    for item in date_separ:
        date_separ[i] = int(date_separ[i])
        i = i +1

    date_year  = date_separ[0] # type int
    date_month = date_separ[2]
    date_day   = date_separ[1]


    if date_year != today_date_year:
        print("!!! SEEMS THAT YEAR INPUT IS NOT CORRECT !!!")
        return

    if date_month != today_date_month:
        print("!!! SEEMS THAT MONTH INPUT IS NOT CORRECT !!!")
        return

    day_dt = date_day - today_date_day


    if country_code == "CZ":
        city = "Prague"

    elif country_code == "SK":
        city = "Bratislava"

    elif country_code == "UK":
        city = "London"


    days = day_dt + 1

    url = "http://api.weatherapi.com/v1/forecast.json?key=361f4a39a7cb4ab892d131558211807&q={}&days={}"

    response = requests.get(url.format(city, days))

    if response.status_code != 200:
        print("\n \n \n!!! SORRY, CRASHED !!!\n \n \n")

    response = requests.get(url.format(city, days)).json()

    weather = {
        "country": country_code,
        "city": response["location"]["name"],
        "date": response["forecast"]["forecastday"][0]["date"],
        "temp_av": response["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        }

    context = {"weather": weather}


    if context["weather"]["temp_av"] > 20:
        answer = "good"

    elif 10 <= context["weather"]["temp_av"] <= 20:
        answer = "soso"

    else:
        answer = "bad"

    final = {"forecast": answer}


    return JsonResponse(final)


