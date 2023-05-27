from rest_framework import serializers
from article.models import Article, Comment
from . import aiutils


class ArticleSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    image = serializers.ImageField(
        max_length=None,
        use_url=True,
    )
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True,
    )

    def get_user(self, obj):
        nickname = obj.user.nickname
        return nickname

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Article
        fields = (
            "pk",
            "title",
            "content",
            "image",
            "result",
            "user",
            "comments_count",
            "created_at",
        )


class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = (
            "user",
            "image",
            "result",
        )

    def create(self, validated_data):
        article = super().create(validated_data)
        result = aiutils.image_mache(article.image)
        article.result = result
        article.save()
        return article


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True,
    )
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = Comment
        fields = [
            "user",
            "content",
            "created_at",
        ]
