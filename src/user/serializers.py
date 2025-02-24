from rest_framework import serializers
from .models import User
from ..user.models import Level
import cloudinary


class CloudinaryURLField(serializers.Field):
    def to_representation(self, value):
        url = str(value)
        # If the value is already a full URL, return it directly.
        if url.startswith('http'):
            return url
        # Otherwise, assume it's a public id and build the full URL.
        return cloudinary.CloudinaryImage(url).build_url()

    def to_internal_value(self, data):
        return data


class ProfileLevelSerializer(serializers.ModelSerializer):
    level_image = CloudinaryURLField()

    class Meta:
        model = Level
        fields = ['name', 'level_image', 'level_number']


class UserSerializer(serializers.ModelSerializer):
    user_image = CloudinaryURLField()
    level = ProfileLevelSerializer()

    class Meta:
        model = User
        fields = '__all__'
