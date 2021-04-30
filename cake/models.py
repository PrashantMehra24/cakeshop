from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
class cake(models.Model):
    name=models.CharField(max_length=40,default='')
    flavour=models.CharField(max_length=40)
    price=models.IntegerField(default=0)
    weight =models.IntegerField(default=0)
    description=models.CharField(max_length=100,default='')
    eggless=models.BooleanField(default=False)
    category=models.CharField(max_length=20,default='')
    image=models.CharField(max_length=400,default='')
    def __str__(self):
        return self.name

class user(models.Model):
    username=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=50,default='')
    password=models.CharField(max_length=20,default='')

    def __str__(self):
        return self.username


class cart(models.Model):
    cakeid = models.IntegerField()
    orderdate = models.DateTimeField(default=datetime.now, blank=True)
    image = models.CharField(max_length=100 )
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1,blank=True,null=True)
    weight = models.FloatField()
    email = models.EmailField()
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    orderdate = models.DateTimeField(default=datetime.now, blank=True)
    address = models.CharField(max_length=255)
    pincode = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    price = models.IntegerField()
    pending = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    mode = models.CharField(default="Cash",max_length=20)
    cakes = models.ManyToManyField(cart)

    def __str__(self):
        return self.email

