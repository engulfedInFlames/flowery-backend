from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from article.models import Article, Comment, Photos
from article.serializers import ArticleCreateSerializer, ArticleSerializer, CommentSerializer, ArticleDetailSerializer


class ArticleList(APIView):
    def get(self, request):
        article = Article.objects.all()
        article_serialize = ArticleSerializer(article, many=True)

        return Response({'article': article_serialize.data, }, status=status.HTTP_200_OK)

    def post(self, request):
        permission_classes = [IsAuthenticated]

        serialize = ArticleCreateSerializer(
            data=request.data, context={'request': request})
        if serialize.is_valid():
            serialize.save(user=request.user)
            return Response(serialize.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': f'${serialize.errors}'}, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        comment = Comment.objects.filter(article=pk)
        article_serialize = ArticleDetailSerializer(article)
        comment_serialize = CommentSerializer(comment, many=True)
        return Response({'article': article_serialize.data, 'comment': comment_serialize.data}, status=status.HTTP_200_OK)


class ToggleArticleLike(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return Response({'message': '취소'}, status=status.HTTP_202_ACCEPTED)
        else:
            article.likes.add(request.user)
            return Response({'message': '좋아요'}, status=status.HTTP_200_OK)


class CreateComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serialize = CommentSerializer(data=request.data)
        article = Article.objects.get(id=pk)
        if serialize.is_valid():
            serialize.save(user=request.user, article=article)
            return Response({'message': '댓글 작성 완료'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': f'${serialize.errors}'}, status=status.HTTP_400_BAD_REQUEST)