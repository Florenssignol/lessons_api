from rest_framework import serializers

from django.contrib.auth.models import User
from lessons.models import Lesson, Account, Subscription, Status, Students

class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    description = serializers.CharField(max_length=200)
    insert_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(queryset=Subscription.objects.all())
    lesson_locked = serializers.BooleanField()

    def create(self, validated_data):
        return Lesson.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        instance.insert_date = validated_data.get('insert_date', instance.insert_date)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    address = serializers.CharField()
    insert_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.address = validated_data.get('address', instance.address)
        instance.insert_date = validated_data.get('insert_date', instance.insert_date)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance

class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subscription_date = serializers.DateTimeField()
    insert_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)
    account_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())

    def create(self, validated_data):
        return Subscription.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.subscription_date = validated_data.get('subscription_date', instance.subscription_date)
        instance.insert_date = validated_data.get('insert_date', instance.insert_date)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance

class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    insert_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Status.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.insert_date = validated_data.get('insert_date', instance.insert_date)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance

class StudentsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField()
    email = serializers.CharField()
    insert_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)
    account_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())

    def create(self, validated_data):
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.email = validated_data.get('email', instance.email)
        instance.insert_date = validated_data.get('insert_date', instance.insert_date)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance
