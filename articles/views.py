from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_200_OK,
)
from .models import Article
from .serializers import ArticleSerializer


class Articles(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # JSON 형식으로 보내면 우선 유효한 Response를 받을 수 있다.
        # article = articles[0]
        # context = {
        #     "title": article.title,
        #     "content": article.content,
        # }
        return Response(serializer.data, status=HTTP_200_OK)
        # error를 다 보여주는 것은 바람직하지 않다.

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = serializer.save()
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Article, id=id)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(
            article,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            article = serializer.save()
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=HTTP_204_NO_CONTENT)
