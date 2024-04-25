from django.db import models
from django.contrib.auth.models import User
from home.models import *

# Create your models here.

class ProductRating(models.Model):
    rate_sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='rateProductSender')
    rate_product = models.ForeignKey(Car, on_delete=models.CASCADE,related_name='rateProduct')
    rate_content = models.TextField()

    def __str__(self):
        return self.rate_content