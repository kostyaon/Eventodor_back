from django.contrib import admin
from .models import Photo, User, Event, UserEvent

# Register your models here.
admin.site.register([User, Event, UserEvent, Photo])