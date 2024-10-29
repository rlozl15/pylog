from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from blog.models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
        comment_content = request.POST.get("content")
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    context = {
        "post":post
    }
    return render(request,"post_detail.html", context)

def post_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        thumbnail = request.FILES.get("thumbnail")
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
        )
        return redirect(f"/posts/{post.id}/")
    return render(request, "post_add.html")