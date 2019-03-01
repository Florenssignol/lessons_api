from rest_framework import serializers 

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Userfields = ('id', 'username', 'email')