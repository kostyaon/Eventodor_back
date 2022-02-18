from django.contrib import admin
from .models import Category, Coordinate, FavouriteEvents, OrgEvent, Organization, Organizer, Photo, Review, User, Event, UserEvent

# Register your models here.
admin.site.register([
    User, Event, UserEvent,
    Photo, Review, FavouriteEvents,
    Coordinate, Category, Organization,
    Organizer, OrgEvent
 ])