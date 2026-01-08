from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.view_posts, name="view_posts"),
    path("create_post/", views.create_post, name="create_post"),
]
