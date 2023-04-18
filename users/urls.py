from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view(), name="all_users"),
    path("<int:id>", views.User.as_view(), name="only_one_user"),
]
