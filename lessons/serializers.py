from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from django.contrib.auth.models import User
from lessons.models import Lesson

class UserSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class LessonSerializer(serializers.HyperLinkedModelSerializer):
    class Meta: 
        model = Lesson
        fields = ('lesson_id', 'date', 'description')