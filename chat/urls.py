from django.urls import path
from . import views

app_name = "Chat"

urlpatterns = [
    path("", views.chat, name="chat"),
    path("new/<user_id>", views.new_chat, name="new_chat"),
    path("<room_id>", views.chat, name="chat"),
]