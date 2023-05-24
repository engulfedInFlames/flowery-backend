from django.db import models
from users.models import CustomUser


class Article(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    # ✅ photo = models.Foreignkey()
    # ✅ result = models.Charfield(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(
        CustomUser,
        blank=True,
        symmetrical=False,
    )

    def __str__(self) -> str:
        return f"게시글 #{self.pk}"

    class Meta:
        verbose_name_plural = "게시글들"


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"댓글 #{self.pk}"

    class Meta:
        verbose_name_plural = "댓글들"


# ✅ 모델명 Photos => Photo
# ✂️ Photo 모델에 article 필드 제거하고, article 필드에 photo 모델을 ForeignKey로 등록. related_name은 "article"
# ✅ 수정된 내용 serializers, views, urls 반영


class Photos(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    image = models.ImageField(
        upload_to="article/%Y/%m/%d",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"사진 #{self.pk}"

    class Meta:
        verbose_name_plural = "사진들"
