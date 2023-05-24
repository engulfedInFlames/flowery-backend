from rest_framework import serializers
from article.models import Article, Comment, Photo


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "image",
        ]


class ArticleSerializer(serializers.ModelSerializer):
<<<<<<< Updated upstream
    # ✅ 좋아요를 누른 유저들의 pk 리스트, 변수명: like_users_pk
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        image = obj.photos.first()
        return ImageSerializer(instance=image).data

    class Meta:
        model = Article
        fields = (
            "pk",
            "title",
            "content",
            "image",
            "user",
            "created_at",
        )


class ArticleDetailSerializer(serializers.ModelSerializer):
    # ✅ 댓글 개수, 변수명: comments_count
    image = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_image(self, obj):
        image = obj.photos.all()
        return ImageSerializer(instance=image, many=True).data

    def get_comments_count(self, obj):
        count = Comment.objects.filter(article__pk=obj.pk).count()
        return count

=======
>>>>>>> Stashed changes
    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ["user", "likes", "image", "result"]


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
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
