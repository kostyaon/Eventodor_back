from unicodedata import category
from django import views
from rest_framework import generics, viewsets
from .models import Category, Coordinate, FavouriteEvents, OrgEvent, Organization, Organizer, Review, User, Event, UserEvent, Photo
from .serializers import CategorySerializer, CoordinateSerializer, FavouriteEventSerializer, OrgEventSerializer, OrganizationSerializer, OrganizerSerializer, PhotoSerializer, ReviewSerializer, SetReviewSerializer, UserEventSerializer, UserSerializer, EventSerializer

# Create your views here.

class UserIdViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user_id = self.request.user.id
        myAccount = queryset.filter(id=user_id)
        return myAccount

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
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ReviewSerializer
        if self.action == 'create':
            return SetReviewSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavouriteEventSerializer

    def get_queryset(self):
        queryset = FavouriteEvents.objects.all()
        user_param = self.request.GET.get('userId')
        if user_param:
            queryset = queryset.filter(user_id=user_param)
        
        return queryset


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class OrgEventViewSet(viewsets.ModelViewSet):
    queryset = OrgEvent.objects.all()
    serializer_class = OrgEventSerializer