from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from lessons.models import Lesson, Account, Subscription, Status, Students

from lessons.serializers import LessonSerializer, AccountSerializer, SubscriptionSerializer, StatusSerializer, StudentsSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

def home(request): 
    return HttpResponse("<h1>Home</h1>")

class LessonView(APIView):
    def get(self, request):
        queryset = Lesson.objects.all()
        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AccountView(APIView):
    def get(self, request):
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubscriptionView(APIView):
    def get(self, request):
        queryset = Subscription.objects.all()
        serializer = SubscriptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StatusView(APIView):
    def get(self, request):
        queryset = Status.objects.all()
        serializer = StatusSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentsView(APIView):
    def get(self, request):
        queryset = Students.objects.all()
        serializer = StudentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# class ListUserView(listAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         if user_id is not None:
#             return User.objects.filter(id=user_id)
#         return User.objects.all()
