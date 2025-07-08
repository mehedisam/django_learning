from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data={
            'username':'samee',
            'email':'samee@g.com',
            'password':'shohanakash',
            'password2':'shohanakash'
        }
        response=self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
