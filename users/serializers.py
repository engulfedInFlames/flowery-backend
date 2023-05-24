from rest_framework import serializers
from rest_framework.exceptions import ParseError

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(self, user):
        token = super().get_token(user)
        token["email"] = user.email
        print(token)

        return token


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "nickname",
            "password",
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        nickname = user.nickname

        if not password:
            raise ParseError

        if not nickname:
            nickname = f"user#{user.pk}"
            user.nickname = nickname

        user.set_password(password)
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "nickname",
<<<<<<< Updated upstream
            "is_active",
=======
            "password"
>>>>>>> Stashed changes
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        write_only_fields = ("password",)

    def update(self, user, validated_data):
        user = super().update(user, validated_data)
        password = user.password

        if password is None:
            raise ParseError

        user.set_password(password)
        user.save()

        return user
