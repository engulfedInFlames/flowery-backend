from django.urls import reverse
from rest_framework.test import APITestCase
from .models import CustomUser


class CreateUSerTest(APITestCase):
    USER_DATA = {
        "email": "sparta100@naver.com",
        "nickname": "spartaTest100",
        "password": "sparta",
    }

    def test_create_user(self):
        response = self.client.post(reverse("user_list"), self.USER_DATA)
        self.assertEqual(response.status_code, 200)


class LoginUserTest(APITestCase):
    USER_DATA = {
        "email": "sparta100@naver.com",
        "nickname": "spartaTest100",
        "password": "sparta",
    }

    def setUp(self):
        self.user = CustomUser.objects.create_user("sparta100@naver.com", "sparta")

    def test_login(self):
        response = self.client.post(reverse("token_obtain_pair"), self.USER_DATA)
        self.assertEqual(response.status_code, 200)

    def test_get_user_data(self):
        response = self.client.post(reverse("token_obtain_pair"), self.USER_DATA)
        access_token = response.data.get("access")

        response = self.client.get(
            path=reverse("user_list"), HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        self.assertEqual(response.status_code, 200)
