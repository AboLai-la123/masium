# Generated by Django 4.2.9 on 2024-04-18 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_description', models.TextField()),
                ('car_brand', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_type', models.CharField(max_length=50)),
                ('car_model_year', models.IntegerField()),
                ('car_maintenance', models.BooleanField(default=False)),
                ('car_status', models.CharField(max_length=20)),
                ('car_walkway', models.IntegerField()),
                ('car_interior', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.ImageField(upload_to='cars')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.car')),
            ],
        ),
    ]
