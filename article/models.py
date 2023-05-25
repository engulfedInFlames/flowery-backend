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
    image = models.ImageField(
        upload_to="images/%Y/%m/%d",
        null=True,
        blank=True,
    )
    result = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"게시글 #{self.pk}"

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

    def __str__(self) -> str:
        return f"댓글 #{self.pk}"

    class Meta:
        verbose_name_plural = "댓글들"
