from dataclasses import field
from rest_framework import serializers
from .models import User, Event, UserEvent

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'name', 'surname', 
            'patronymic', 'phone', 'email',
            'country', 'city', 'address', 'bankAccount'
             )

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id', 'address', 'persons_amount', 'register_persons_amount',
            'name', 'description', 'time',
            'price', 'rank'
        )

class UserEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserEvent
        fields = (
            'user_id', 'event_id'
        )