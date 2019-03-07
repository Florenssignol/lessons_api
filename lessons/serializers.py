from rest_framework import serializers

from django.contrib.auth.models import User
from lessons.models import Lesson, Account, Subscription, Status, Students

class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateTimeField()
    description = serializers.CharField(max_length=200)
    insert_date = serializers.DateField()
    update_date = serializers.DateTimeField()

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    address = serializers.CharField()
    insert_date = serializers.DateField()
    update_date = serializers.DateTimeField()

class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    subscription_date = serializers.DateTimeField()
    insert_date = serializers.DateField()
    update_date = serializers.DateTimeField()

class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    insert_date = serializers.DateField()
    update_date = serializers.DateTimeField()

class StudentsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField()
    email = serializers.CharField()
    insert_date = serializers.DateField()
    update_date = serializers.DateTimeField()