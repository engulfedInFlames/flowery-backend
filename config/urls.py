from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import GetCSRFToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/articles/", include("article.urls")),
    path("api/v1/get-csrftoken/", GetCSRFToken.as_view(), name="get_csrftoken"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
