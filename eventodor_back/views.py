from django import views
from rest_framework import generics, viewsets
from .models import User, Event, UserEvent, Photo
from .serializers import PhotoSerializer, UserEventSerializer, UserSerializer, EventSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class UserEventViewSet(viewsets.ModelViewSet):
    serializer_class = UserEventSerializer

    def get_queryset(self):
        queryset = UserEvent.objects.all()
        user_param = self.request.GET.get('userId')
        event_param = self.request.GET.get('eventId')
        if user_param:
            queryset = queryset.filter(user_id=user_param)
        
        if event_param:
            queryset = queryset.filter(event_id=event_param)
        
        return queryset

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
        