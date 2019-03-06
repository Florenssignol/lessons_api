from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from lessons.models import Lesson

from lessons.serializers import LessonSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

import json

def home(request): 
    return HttpResponse("<h1>Home</h1>")

# class ListUserView(listAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         if user_id is not None:
#             return User.objects.filter(id=user_id)
#         return User.objects.all()

class LessonView(APIView):
    def get(self, request):
        queryset = Lesson.objects.all()
        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
