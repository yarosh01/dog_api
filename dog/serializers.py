from rest_framework import serializers
from rest_captcha.serializers import RestCaptchaSerializer

from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class DogPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ["photo"]

    def save(self, *args, **kwargs):
        if self.instance.photo:
            self.instance.photo.delete()
        return super().save(*args, **kwargs)
