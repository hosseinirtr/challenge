from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterViewTestCase(APITestCase):
    url = reverse('register')

    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email": "testuser@test.com",
            "password": "testpassword"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')
        
class ObtainTokenViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.url = reverse('api_token_auth')

    def test_obtain_token(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'testpass'})
        token = Token.objects.get(user=self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'token': token.key})