from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path("", views.home, name="home"),
    path("components", views.components, name="components"),
    path("profile", views.profile, name="profile"),
    path("favorite", views.favorite, name="favorite"),
    path("notifications", views.notifications, name="notifications"),
    path("<brandName>", views.category, name="category"),
]