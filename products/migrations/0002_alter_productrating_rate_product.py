# Generated by Django 4.2.9 on 2024-04-21 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rating'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrating',
            name='rate_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rateProduct', to='home.car'),
        ),
    ]