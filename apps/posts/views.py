from django.shortcuts import render
from .models import Post


def view_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


def view_post(request):
    pass


def create_post(request):
    pass


def edit_post(request):
    pass


def delete_post(request):
    pass
