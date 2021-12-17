from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username": "test",
            "email": "test@gmail.com",
            "password": "t.123456",
            "password2": "t.123456",
        }

        url = reverse('register')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password="t.123456")

    def test_login(self):
        data = {
            "username": "test",
            "password": "t.123456",
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)
        self.token = Token.objects.get(user__username='test')
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)

        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
