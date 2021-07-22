from django.urls import path

from weather_forecast import views



urlpatterns = [
    path("", views.index, name = "index"),
]


