from rest_framework import serializers

from django.contrib.auth.models import User
from lessons.models import Lesson

class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateTimeField()
    description = serializers.CharField(max_length=200)
    insert_date = serializers.DateField()
    update_date = serializers.DateTimeField()