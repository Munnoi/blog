from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post


def view_posts(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, "posts/index.html", {"posts": posts})


def view_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "posts/detail.html", {"post": post})


@login_required(login_url="accounts:login")
def create_post(request):
    print(request.method)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content, author=request.user) # This saves the data in db
        return redirect("posts:view_posts")
    return render(request, "posts/create_post.html")


def edit_post(request):
    pass


def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect("posts:view_posts")
    
