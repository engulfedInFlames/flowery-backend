import os
import dotenv
import requests

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import (
    UserSerializer,
    CreateUserSerializer,
    CustomTokenObtainPairSerializer,
)

env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(CustomUser, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_200_OK)


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class GithubLogin(APIView):
    def post(self, request):
        code = request.data.get("code", None)

        token_url = "https://github.com/login/oauth/access_token"

        # ✅ 자신이 설정한 redirect_uri를 할당
        redirect_uri = "http://3.34.155.8/github-login"

        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        response = requests.post(
            token_url,
            data={
                "client_id": os.environ.get("GH_CLIENT_ID"),
                "client_secret": os.environ.get("GH_CLIENT_SECRETS"),
                "code": code,
                "redirect_uri": redirect_uri,
            },
            headers={
                "Accept": "application/json",
            },
        )

        access_token = response.json().get("access_token")
        user_url = "https://api.github.com/user"
        user_email_url = "https://api.github.com/user/emails"

        response = requests.get(
            user_url,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json",
            },
        )
        user_data = response.json()
        response = requests.get(
            user_email_url,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json",
            },
        )

        user_emails = response.json()

        user_email = None
        for email_data in user_emails:
            if email_data.get("primary") and email_data.get("verified"):
                user_email = email_data.get("email")

        try:
            user = CustomUser.objects.get(email=user_email)

            refresh_token = CustomTokenObtainPairSerializer.get_token(user)

            return Response(
                {
                    "refresh": str(refresh_token),
                    "access": str(refresh_token.access_token),
                }
            )

        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_user(email=user_email)
            user.nickname = user_data.get("login", f"user#{user.pk}")
            user.avatar = user_data.get("avatar_url", None)
            user.set_unusable_password()
            user.save()

            refresh_token = CustomTokenObtainPairSerializer.get_token(user)

            return Response(
                {
                    "refresh": str(refresh_token),
                    "access": str(refresh_token.access_token),
                }
            )
