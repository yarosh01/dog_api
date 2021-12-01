from rest_framework import serializers
from rest_captcha.serializers import RestCaptchaSerializer
from .models import Dog, Breed


class HumanOnlyDataSerializer(RestCaptchaSerializer):
    pass


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
