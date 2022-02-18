from dataclasses import field, fields
from rest_framework import serializers
from .models import Category, Coordinate, FavouriteEvents, OrgEvent, Organization, Organizer, Photo, Review, User, Event, UserEvent

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'photo_id',
            'name', 'surname', 
            'patronymic', 'phone', 'email',
            'country', 'city', 'address', 'bankAccount'
             )

class UserEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserEvent
        fields = (
            'user_id', 'event_id'
        )

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = (
            'id', 'url'
        )

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'id', 'event_id', 'user_id',
            'description', 'rank'
        )

class FavouriteEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouriteEvents
        fields = (
            'user_id', 'event_id'
        )

class CoordinateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordinate
        fields = (
            'id', 'longitude',
            'latitude', 'height'
        )

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id', 'name'
        )

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = (
            'id', 'name', 'description',
            'phone', 'email', 'bankAccount'
        )

class OrganizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizer
        fields = (
            'id', 'photo_id', 'building_id',
            'name', 'surname', 'patronymic',
            'phone', 'email', 'country', 
            'city', 'address', 'bankAccount'
        )

class OrgEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgEvent
        fields = (
            'org_id', 'event_id'
        )
        
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id', 'photo', 'coordinate', 'category', 'organizer',
            'address', 'persons_amount', 'register_persons_amount',
            'name', 'description', 'time',
            'price', 'rank'
        )
        depth = 1