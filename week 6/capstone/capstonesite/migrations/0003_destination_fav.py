# Generated by Django 3.1.4 on 2021-04-23 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capstonesite', '0002_destination2_destination3'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='fav',
            field=models.ManyToManyField(related_name='fav_destinations', to=settings.AUTH_USER_MODEL),
        ),
    ]
