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
        print(response.data)
        self.assertEqual(response.status_code, 200)

    # def test_something_that_will_pass(self):
    #     self.assertFalse(False)

    # def test_something_that_will_fail(self):
    #     self.assertTrue(False)


class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {
            "email": "sparta101@naver.com",
            "nickname": "spartaTest101",
            "password": "password",
        }
        self.user = CustomUser.objects.create_user(
            "sparta101@naver.com", "password")

    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        print(response.data["access"])
        self.assertEqual(response.status_code, 200)
