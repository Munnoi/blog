from django.shortcuts import render, redirect
from .models import Post


def view_posts(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, "posts/index.html", {"posts": posts})


def view_post(request):
    pass


def create_post(request):
    print(request.method)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content) # This saves the data in db
        return redirect("view_posts")
    return render(request, "posts/create_post.html")


def edit_post(request):
    pass


def delete_post(request):
    pass
