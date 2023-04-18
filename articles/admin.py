from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAmdin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
    )
