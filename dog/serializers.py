from rest_framework import serializers

from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ["name", "age", "breed", "gender", "color", "favoritefood", "favoritetoy"]


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
