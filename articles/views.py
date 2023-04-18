from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
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

        return Response(serializer.data)
