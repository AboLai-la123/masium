# Generated by Django 4.2.9 on 2024-04-18 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarImages',
            new_name='CarImage',
        ),
    ]
