from rest_framework import serializers
from .models import User, Event

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
            'address', 'persons_amount', 'register_persons_amount',
            'name', 'description', 'time',
            'price', 'rank'
        )