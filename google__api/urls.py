from django.urls import path
from . import views

app_name = "google__api"

urlpatterns = [
    path('route', views.route, name="route"),
    path('map', views.map, name="map"),
]