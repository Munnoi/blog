from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post


@login_required(login_url="accounts:login")
def view_posts(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, "posts/index.html", {"posts": posts})


@login_required(login_url="accounts:login")
def view_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "posts/detail.html", {"post": post})


@login_required(login_url="accounts:login")
def create_post(request):
    print(request.method)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(
            title=title, content=content, author=request.user
        )  # This saves the data in db
        return redirect("posts:view_posts")
    return render(request, "posts/create_post.html")


@login_required(login_url="accounts:login")
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post")
    
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post.title = title
        post.content = content
        post.save()
        return redirect("posts:view_posts")
    return render(request, "posts/edit_post.html", {"post": post})


@login_required(login_url="accounts:login")
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post")
    
    if request.method == "POST":
        post.delete()
        return redirect("posts:view_posts")
