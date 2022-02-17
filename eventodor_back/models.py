
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.url

class Coordinate(models.Model):
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    height = models.CharField(max_length=100)

    def __str__(self):
        return self.longitude

class Event(models.Model):
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
    coordinate_id = models.ForeignKey(Coordinate, on_delete=models.CASCADE)
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

class User(models.Model):
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
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

class UserEvent(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)

class Review(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    rank = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.description

class FavouriteEvents(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)