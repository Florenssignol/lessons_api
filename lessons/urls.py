"""florence_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
#from django.contrib import admin
from django.urls import path 
from . import views

from django.contrib.auth.models import User

from lessons.views import LessonView, AccountView, SubscriptionView, StatusView, StudentsView

# from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'subscription', SubscriptionView, base_name = "subscription")
# router.register(r'account', AccountView, base_name = "account")
# urlpatterns = router.urls

urlpatterns = [
    path('', views.home, name='home'),

    path('account/<int:pk>', AccountView.as_view(), name='account/student'),
    path('account/create', AccountView.as_view()),

    path('dashboard/create_sub', SubscriptionView.as_view()),
    path('dashboard/update_status', SubscriptionView.as_view()),

    path('dashboard/create_lesson', LessonView.as_view()),
    path('dashboard/<subscription_id>', LessonView.as_view(), name='subscription/lesson'),

    path('account/create_student', StudentsView.as_view()),
    path('dashboard/enroll_student', StudentsView.as_view(), name='student_lessons'),

    path('dashboard/lesson/<id>', StudentsView.as_view()),
    
    #path('user/<user_id>', ListUserView.as_view()),
    # path('lessons/', LessonView.as_view()),
    # path('account/', AccountView.as_view()),
    # path('subscription/', SubscriptionView.as_view()),
    # path('status/', StatusView.as_view()),
    # path('students/', StudentsView.as_view()),
    # path('account/delete_student/<student_id>', StudentsView.as_view()),

]
