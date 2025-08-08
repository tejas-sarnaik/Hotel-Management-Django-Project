from django.db import models
# Create your models here.
class People(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mbl=models.CharField(max_length=200)
    checkin=models.CharField(max_length=200)
    checkout=models.CharField(max_length=200)
    guests=models.CharField(max_length=200)
    roomtype=models.CharField(max_length=200)
    identitytype=models.CharField(max_length=200)
    identityproof=models.CharField(max_length=200)
    