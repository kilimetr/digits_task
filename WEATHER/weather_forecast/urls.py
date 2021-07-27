from django.urls import path, re_path

from weather_forecast import views



urlpatterns = [
    path("", views.index, name = "index"),
    re_path(r"^(?P<date>[\w-]+)/(?P<country_code>[\w-]+)/$", views.jresp_result, name = "jresp_result")
    # re_path(r"^[\w-]+/$", views.jresp_result, name = "jresp_result")
]


