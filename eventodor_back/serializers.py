from dataclasses import field, fields
from rest_framework import serializers
from .models import Coordinate, FavouriteEvents, Photo, Review, User, Event, UserEvent

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'photo_id',
            'name', 'surname', 
            'patronymic', 'phone', 'email',
            'country', 'city', 'address', 'bankAccount'
             )

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id', 'photo_id', 'coordinate_id',
            'address', 'persons_amount', 'register_persons_amount',
            'name', 'description', 'time',
            'price', 'rank'
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