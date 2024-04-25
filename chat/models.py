from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")
    room_new_messages = models.IntegerField(default=0)
    room_last_message = models.CharField(max_length=100)

class Chat(models.Model):
    chat_user = models.ForeignKey(User, on_delete = models.CASCADE)
    chat_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    chat_message = models.TextField()