from django.contrib import admin

from .models import Article, Comment, Photo


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk",)


@admin.register(Photo)
class PhotosAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "image",
    )
