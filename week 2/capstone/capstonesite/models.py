from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):   
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    los = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')
    fav = models.ManyToManyField(User, related_name='fav_destinations1')
    
class Destination2(models.Model):
    
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    los = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')
    fav = models.ManyToManyField(User, related_name='fav_destinations2')

class Destination3(models.Model):
    
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    los = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')
    fav = models.ManyToManyField(User, related_name='fav_destinations3')


    