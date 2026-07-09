from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class UserRegistrationTests(APITestCase):

    def test_user_registration(self):
        url = reverse("register")

        data = {
            "username": "testuser",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "password123",
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "testuser")
