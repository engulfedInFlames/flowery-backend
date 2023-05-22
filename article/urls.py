from django.urls import path, include
from article import views

urlpatterns = [
    path("", views.ArticleList.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetail.as_view(), name="article_detail"),
    path("<int:pk>/comments/",
         views.CreateComment.as_view(), name="article_comment"),
    path("<int:pk>/like/", views.ToggleArticleLike.as_view(), name="article_like"),
]
