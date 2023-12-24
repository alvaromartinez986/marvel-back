from rest_framework import serializers
from .models import Character, Comic, ApiStatus

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'

class ApiStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiStatus
        fields = ['data_loaded']

