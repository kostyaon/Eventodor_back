from django.contrib import admin
from .models import User, Event, UserEvent

# Register your models here.
admin.site.register([User, Event, UserEvent])