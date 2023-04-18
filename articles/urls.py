from django.urls import path
from . import views

urlpatterns = [
    path("", views.Articles.as_view(), name="all_articles"),
    path("<int:id>", views.ArticleDetail.as_view(), name="only_one_article"),
]
