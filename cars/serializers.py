from rest_framework import serializers
from .models import Cars, Cardata, NewUser

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

class CardataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardata
        fields = '__all__'

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        exclude = ['user_password', 'reset_token']
