from django.urls import path
from . import views

app_name = "Cars"

urlpatterns = [
    path("add-car", views.addCar, name="addCar"),
]