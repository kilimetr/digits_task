from django.forms import ModelForm, TextInput
from weather_forecast.models import Weather_Update



class Weather_Update_Form(ModelForm):
    class Meta:
        model = Weather_Update
        fields = ["country"]
        widgets = {"country": TextInput(attrs = {"class": "input", "placeholder": "Weather Country"}),}

