from dataclasses import field, fields
from unicodedata import category, name
from django.forms import IntegerField
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
    category = CategorySerializer()
    coordinate = CoordinateSerializer()
    organizer = OrganizerSerializer()

    class Meta:
        model = Event
        fields = (
            'id', 'photo', 'coordinate', 'category', 'organizer',
            'address', 'persons_amount', 'register_persons_amount',
            'name', 'description', 'time',
            'price', 'rank'
        )
        depth = 1
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        newCategory = Category.objects.create(**category_data)
        coordinate_data = validated_data.pop('coordinate')
        newCoordinate = Coordinate.objects.create(**coordinate_data)
        organizer_data = validated_data.pop('organizer')
        newOrganizer = Organizer.objects.create(**organizer_data)
        event = Event.objects.create(category=newCategory, coordinate=newCoordinate, organizer=newOrganizer, **validated_data)
        return event

class SetReviewSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Review
        fields = (
            'id', 'event_id', 'user_id',
            'description', 'rank'
        )
    
    def create(self, validated_data):
        user_data = validated_data.pop('user_id')
        event_data = validated_data.pop('event_id')
        review = Review.objects.create(event_id=event_data, user_id=user_data, **validated_data)
        return review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'id', 'event_id', 'user_id',
            'description', 'rank'
        )
        depth = 1
