from django.db import models
from users.models import CustomUser


class Article(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 좋아요
    likes = models.ManyToManyField(
        CustomUser,
        blank=True,
        symmetrical=False,
    )

    class Meta:
        verbose_name_plural = "게시글들"


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "댓글들"


class Photos(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    image = models.ImageField(
        upload_to="article/%Y/%m/%d",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "사진들"
