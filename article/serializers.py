from rest_framework import serializers
from article.models import Article, Comment, Photo


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "image",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        image = obj.image
        return ImageSerializer(instance=image).data['image']

    def get_user(self, obj):
        return obj.user.email

    def get_comments_count(self, obj):
        count = Comment.objects.filter(article__pk=obj.pk).count()
        return count

    class Meta:
        model = Article
        fields = "__all__"


class CreateArticleSerializer(serializers.ModelSerializer):
    article_photo = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        exclude = ["user", "likes", "image", "result"]


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)
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
