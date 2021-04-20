from django.db import models

class Destination(models.Model):
    
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    los = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')
    
class Destination2(models.Model):
    
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    los = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')

class Destination3(models.Model):
    
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    los = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')