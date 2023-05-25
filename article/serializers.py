from rest_framework import serializers
from article.models import Article, Comment, Photos
from article import aiutils


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Photos
        fields = [
            "image",
        ]


class ArticleSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    article_photo = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        exclude = ["user", "likes"]

    def create(self, validated_data):
        
        instance = Article.objects.create(**validated_data)
        image_set = self.context["request"].FILES
        content = {}
        for image_data in image_set.getlist("image"):
            img = Photos.objects.create(article=instance, image=image_data)
            content = aiutils.image_mache(img.image)
        instance.content = content
        return instance


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
