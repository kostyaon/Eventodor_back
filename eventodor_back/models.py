from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    bankAccount = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    address = models.CharField(max_length=100)
    persons_amount = models.IntegerField()
    register_persons_amount = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=1)
    rank = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name