# Generated by Django 4.2.9 on 2024-04-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_car_car_seller_car_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
