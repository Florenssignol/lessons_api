from rest_framework import serializers

from django.contrib.auth.models import User
from lessons.models import Lesson

class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateTimeField(auto_now=False)
    description = serializers.CharField(max_length=200, null=False)
    subscription_id = serializers.ForeignKey(
        'Subscription', 
        on_delete=models.CASCADE,
    )
    insert_date = serializers.DateField(auto_now=True)
    update_date = serializers.DateTimeField(auto_now=True)