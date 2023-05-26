from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser


class UserRegistrationTest(APITestCase):
 #  ✅ test용 기본 가입된 계정
    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "identify": "default_user",
            "email": "sparta_default@naver.com",
            "nickname": "spartaTest_default",
            "password": "password_default",
        }
        cls.user = CustomUser.objects.create_user(
            "sparta_default@naver.com", "password_default")

 #  ✅ 일반 회원가입 : 이메일, 닉네임, 비밀번호
    def test_registration(self):
        url = reverse("user_list")
        user_data = {
            "identify": "user_signup_test",
            "email": "sparta100@naver.com",
            "nickname": "spartaTest100",
            "password": "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 200)

#  ✅ userlist
    def test_registration_list(self):
        url = reverse("user_list")
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, 200)


class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {
            "email": "sparta101@naver.com",
            "nickname": "spartaTest101",
            "password": "password",
        }
        self.user = CustomUser.objects.create_user(
            "sparta101@naver.com", "password")

#  ✅ 로그인
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_user_data(self):
        access_token = self.client.post(
            reverse('token_obtain_pair'), self.data).data["access"]
        response = self.client.get(
            path=reverse('user_list'),
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data['email'], self.data['email'])
