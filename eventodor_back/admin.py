from django.contrib import admin
from .models import Coordinate, FavouriteEvents, Photo, Review, User, Event, UserEvent

# Register your models here.
admin.site.register([
    User, Event, UserEvent,
    Photo, Review, FavouriteEvents,
    Coordinate, 
 ])