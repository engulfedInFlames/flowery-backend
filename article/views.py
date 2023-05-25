from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from article.models import Article, Comment, Photo
from article import serializers
from django.db.models import Max


class ArticleList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        article = Article.objects.all()
        article_serialize = serializers.ArticleSerializer(article, many=True)

        return Response(
            {
                "articles": article_serialize.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        data = request.data
        image_serialize = serializers.ImageSerializer(data=request.data)
        result = 'a'

        if image_serialize.is_valid():
            image_serialize.save()
            last_id = Photo.objects.aggregate(max_id=Max('id'))['max_id']
            image = Photo.objects.get(id=last_id)

            data.pop('image')
            data_serialize = serializers.CreateArticleSerializer(data=data)
            if data_serialize.is_valid():
                data_serialize.save(user=request.user,
                                    image=image, result=result)
                return Response({'article': data_serialize.data, 'image': image_serialize.data}, status=status.HTTP_200_OK)

            else:
                return Response({"message": f"${data_serialize.errors} "}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"message": f"${image_serialize.data}"}, status=status.HTTP_400_BAD_REQUEST
            )


class ArticleDetail(APIView):
    def get(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        comments = Comment.objects.filter(article=pk)
        article_serialize = serializers.ArticleSerializer(article)
        comments_serialize = serializers.CommentSerializer(comments, many=True)
        return Response(
            {"article": article_serialize.data,
                "comments": comments_serialize.data},
            status=status.HTTP_200_OK,
        )


class ToggleArticleLike(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return Response({"message": "취소"}, status=status.HTTP_202_ACCEPTED)
        else:
            article.likes.add(request.user)
            return Response({"message": "좋아요"}, status=status.HTTP_200_OK)


class CreateComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serialize = serializers.CommentSerializer(data=request.data)
        article = Article.objects.get(pk=pk)
        if serialize.is_valid():
            serialize.save(
                user=request.user,
                article=article,
            )
            return Response(status=status.HTTP_200_OK)
        else:
            print(serialize.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
