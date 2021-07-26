from django.urls import path

from weather_forecast import views



urlpatterns = [
    path("", views.index, name = "index"),
    path("?date={<date>}&country_code={<country_code>}", views.jresp_result, name = "jresp_result")
]


