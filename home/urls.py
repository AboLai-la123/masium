from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path("", views.home, name="home"),
    path("search/<search>", views.search, name="search"),
    path("components", views.components, name="components"),
    path("profile", views.profile, name="profile"),
    path("favorite", views.favorite, name="favorite"),
    path("notifications", views.notifications, name="notifications"),
    path("ratings", views.ratings, name="ratings"),
    path("edit-profile", views.edit_profile, name="edit_profile"),
    path("c/<brandName>", views.category, name="category"),
]