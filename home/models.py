from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    car_seller = models.ForeignKey(User, on_delete= models.CASCADE)
    car_name = models.CharField(max_length=100)
    car_description = models.TextField()
    car_brand = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_model_year = models.IntegerField()
    car_maintenance = models.CharField(max_length=20)
    car_status = models.CharField(max_length=20)
    car_walkway = models.IntegerField()
    car_interior = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    car_price = models.FloatField()

    def __str__(self):
        return self.car_name

class CarImage(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to="cars")

class Favorite(models.Model):
    favorite_product = models.ForeignKey(Car, on_delete=models.CASCADE)
    favorite_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Notification(models.Model):
    notification_user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_title = models.CharField(max_length=20)
    notification_description = models.CharField(max_length=50)
    notification_link = models.CharField(max_length=100)
    notification_is_new = models.BooleanField(default=True)

def formChecker(inputs):
    a, errtitle = "work",""
    for i in inputs:
        if i[2]:
            if i[0].strip() == "":
                a = "no"
                errtitle = i[3][0]
        if a == "work":
            if i[1] == "select":
                if i[0] in i[3]:
                    pass
                else:
                    a = "no"
                    errtitle = "يرجى إختيار الخيارات الصحيحة"
            else:
                if len(i[0]) > i[1]:
                    a = "no"
                    errtitle = i[3][1]
    return a, errtitle