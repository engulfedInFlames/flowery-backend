from rest_framework import serializers
from article.models import Article, Comment, Photos


class ImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Photos
        fields = ['image',]


class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        image = obj.photo_article.first()
        return ImageSerializer(instance=image).data

    class Meta:
        model = Article
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        image = obj.photo_article.all()
        return ImageSerializer(instance=image, many=True).data

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    article_photo = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        exclude = ['user', 'likes']

    def create(self, validated_data):
        instance = Article.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            Photos.objects.create(article=instance, image=image_data)
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content",]
