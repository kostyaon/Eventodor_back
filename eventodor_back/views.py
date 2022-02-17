from rest_framework import generics, viewsets
from .models import User, Event, UserEvent
from .serializers import UserEventSerializer, UserSerializer, EventSerializer

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
        if user_param:
            queryset = queryset.filter(user_id=user_param)
        
        return queryset
        