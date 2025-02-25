from rest_framework import serializers
from .models import *
import cloudinary


class CloudinaryURLField(serializers.Field):
    def to_representation(self, value):
        url = str(value)
        if url.startswith('http'):
            return url
        return cloudinary.CloudinaryImage(url).build_url()

    def to_internal_value(self, data):
        return data


class LevelSerializer(serializers.ModelSerializer):
    level_image = CloudinaryURLField()

    class Meta:
        model = Level
        fields = '__all__'


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    achievement_image = CloudinaryURLField()

    class Meta:
        model = Achievement
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    skill_image = CloudinaryURLField()

    class Meta:
        model = Skill
        fields = '__all__'


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = '__all__'

