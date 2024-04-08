from operator import mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    time=models.CharField(max_length=200)
    venue=models.CharField(max_length=200)
    odyesno=models.CharField(max_length=200)
    image= models.ImageField(upload_to='eventimage/',null=True,blank=True)
    requirements=models.CharField(max_length=200)
    email=models.CharField(max_length=500)
    def __str__(self):
        return self.name+" [ "+str(self.venue)+" ]"

