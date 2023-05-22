from django.db import models
from users.models import CustomUser


class Article(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="article_user")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 좋아요
    likes = models.ManyToManyField(
        CustomUser, blank=True, symmetrical=False, related_name='like')


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="comment_user")
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comment_article")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Photos(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="photo_article")
    image = models.ImageField(
        upload_to="article/%Y/%m/%d", blank=True, null=True)
