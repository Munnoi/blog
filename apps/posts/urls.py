from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_posts, name="view_posts"),
]
