from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ParseError
from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "password",
            "is_active",
            "is_superuser",
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password

        if password is None:
            raise ParseError

        user.set_password(password)
        user.save()

        return user

    def update(self, user, validated_data):
        user = super().update(user, validated_data)
        password = user.password

        if password is None:
            raise ParseError

        user.set_password(password)
        user.save()

        return user
