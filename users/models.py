from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email


#  UserManager는 createsuperuser 명령어를 입력했을 때 호출된다.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):  # 2.
        if not email:
            raise ValueError("Users must have an email address")

        # normalize란?
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):  # 3.
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=240,
        validators=[validate_email],
        unique=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
