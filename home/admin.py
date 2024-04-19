from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(Favorite)
admin.site.register(Notification)