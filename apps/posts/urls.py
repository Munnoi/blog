from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.view_posts, name="view_posts"),
    path("create_post/", views.create_post, name="create_post"),
    path("delete_post/<int:post_id>/", views.delete_post, name="delete_post"),
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
    path("<int:post_id>/", views.view_post, name="view_post"),
]
