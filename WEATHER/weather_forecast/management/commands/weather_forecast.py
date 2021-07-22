from django.core.management.base import BaseCommand
import requests
import datetime
from time import strptime
import json


class Command(BaseCommand):
    help = "Displays weather forecast for max 3 days"

    def add_arguments(self, parser):
        parser.add_argument("forecast_date", type = str, help = "Forecast date")
        parser.add_argument("country",       type = str, help = "Forecast country => city")


    def handle(self, *args, **kwargs):
        date = kwargs["forecast_date"]
        country = kwargs["country"]

        today_date       = datetime.date.today()
        today_date_year  = today_date.year # type int
        today_date_month = today_date.month
        today_date_day   = today_date.day

        date       = strptime(date, "%Y-%d-%m")
        date_year  = date.tm_year # type int
        date_month = date.tm_mon
        date_day   = date.tm_mday


        if date_year != today_date_year:
            print("!!! SEEMS THAT YEAR INPUT IS NOT CORRECT !!!")
            return

        if date_month != today_date_month:
            print("!!! SEEMS THAT MONTH INPUT IS NOT CORRECT !!!")
            return

        day_dt = date_day - today_date_day


        if country == "CZ":
            city = "Prague"

        elif country == "SK":
            city = "Bratislava"

        elif country == "UK":
            city = "London"


        days = day_dt + 1

        url = "http://api.weatherapi.com/v1/forecast.json?key=361f4a39a7cb4ab892d131558211807&q={}&days={}"

        response = requests.get(url.format(city, days))

        if response.status_code != 200:
            print("\n \n \n!!! SORRY, CRASHED !!!\n \n \n")

        response = requests.get(url.format(city, days)).json()

        weather = {
            "country": country,
            "city": response["location"]["name"],
            "date": response["forecast"]["forecastday"][day_dt]["date"],
            "temp_av": response["forecast"]["forecastday"][day_dt]["day"]["avgtemp_c"]  
        }

        context = {"weather": weather}


        if context["weather"]["temp_av"] > 20:
            answer = "good"

        elif 10 <= context["weather"]["temp_av"] <= 20:
            answer = "soso"

        else:
            answer = "bad"

        final = {"forecast": answer}

        return json.dumps(final)

