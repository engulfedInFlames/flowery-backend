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
        url = reverse('token_obtain_pair')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_user_data(self):
        access_token = self.client.post(
            reverse('token_obtain_pair'), self.data).data["access"]
        response = self.client.get(
            path=reverse('user_list'),
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        self.assertEqual(response.status_code, 200)


class UserDetailTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # 회원가입된 기본계정
        cls.default = CustomUser.objects.create_user(
            "sparta_default@naver.com", "password_default")
        # 회원가입된 내계정
        cls.user_data = CustomUser.objects.create_user(
            "sparta_001@naver.com", "password_001")
        # 현재 내계정데이터
        cls.login_data = {"email": "sparta_001@naver.com",
                          "password": "password_001"}
        # 수정된 내계정데이터
        cls.put_data = {"email": "sparta_kang@naver.com",
                        "nickname": "KANG", "password": "password_kang"}

    def setUp(self):
        # 내 토큰
        self.access_token = self.client.post(
            reverse('token_obtain_pair'), self.login_data).data["access"]

# #  ✅ id:1번 게시글 상세페이지 들어가기
    def test_get_user(self):
        """
        1. 비로그인 상태에서 상대방 게시글 상세페이지 열람
        2. 로그인 상태에서 상대방 게시글 상세페이지 열람
        """
        response = self.client.get(path=reverse(
            "user_detail", args=[self.default.id]))
        self.assertEqual(response.data["email"], "sparta_default@naver.com")

    def test_put_user(self):
        response = self.client.put(
            path=reverse("user_detail", args=[self.user_data.id]),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data=self.put_data,
        )
        self.assertEqual(response.data["nickname"], "KANG")

    def test_delete_user(self):
        response = self.client.delete(
            path=reverse("user_detail", args=[self.user_data.id]),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 200)
