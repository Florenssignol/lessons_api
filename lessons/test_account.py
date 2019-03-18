from django.test import TestCase

from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase, URLPatternsTestCase
from lessons.models import Account

from django.urls import include, path, reverse

class AccountTests(APITestCase, URLPatternsTestCase): 
    urlpatterns = [
        path('api', include('lessons.urls')),
    ]

    def test_create_account(self):
        """ test if we can create a new account object"""

        url = reverse('account/create')
        data = {
            'name': 'toto', 
            'email': 'toto@gmail.com', 
            'password': 'totoisawesome', 
            'address': 'totos home'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'toto')

    def test_get_account_when_account_exists(self):
        account = Account(
            name='toto',
            email='toto@gmail.com',
            password='totoisawesome',
            address='totos home', 
        )

        account.save()

        url = reverse('account/student', kwargs={'pk': account.id})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_account_when_account_doesnt_exist(self):
        url = reverse('account/student', kwargs={'pk': 0})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)