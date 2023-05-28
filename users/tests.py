from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser


class UserRegistrationTest(APITestCase):
    def test_registration(self):
        user_data = {
            "email": "sparta100@naver.com",
            "nickname": "spartaTest100",
            "password": "password",
        }
        response = self.client.post(reverse("user_list"), user_data)
        self.assertEqual(response.status_code, 200)


class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {
            "email": "sparta101@naver.com",
            "nickname": "spartaTest101",
            "password": "password",
        }
        self.user = CustomUser.objects.create_user("sparta101@naver.com", "password")

    def test_login(self):
        response = self.client.post(reverse("token_obtain_pair"), self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_user_data(self):
        access_token = self.client.post(reverse("token_obtain_pair"), self.data).data[
            "access"
        ]
        response = self.client.get(
            path=reverse("user_list"), HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)
