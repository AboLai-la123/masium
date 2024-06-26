# Generated by Django 4.2.9 on 2024-04-21 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_content', models.TextField()),
                ('rate_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rateSender', to=settings.AUTH_USER_MODEL)),
                ('rate_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rateUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
