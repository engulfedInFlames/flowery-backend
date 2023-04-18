from django.db import models


class Article(models.Model):
    def __str__(self) -> str:
        return str(self.title)

    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
