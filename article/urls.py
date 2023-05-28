from django.urls import path
from article import views

urlpatterns = [
    path(
        "",
        views.ArticleList.as_view(),
        name="article_list",
    ),
    path(
        "<int:pk>/",
        views.ArticleDetail.as_view(),
        name="article_detail",
    ),
    path(
        "<int:pk>/comments/",
        views.CreateComment.as_view(),
        name="article_comments",
    ),
]
