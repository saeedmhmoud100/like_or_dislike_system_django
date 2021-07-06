from django.shortcuts import redirect, render
from django.db.models import Max
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.annotate(max_like=Max('like')).order_by('-max_like')

    context={
        'posts':posts
    }
    return render(request,'home.html',context)

def detail(request,id):
    post =Post.objects.get(id=id)
    context={
        'post':post
    }
    return render(request,'post_detail.html',context)

def like_or_unlike(request,id):
    post = Post.objects.get(id=id)
    if request.user in post.like.all():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
    return redirect('post_detail',id)

def dislike_or_undislike(request,id):
    post = Post.objects.get(id=id)
    if request.user in post.dislike.all():
        post.dislike.remove(request.user)
    else:
        post.dislike.add(request.user)
    return redirect('post_detail',id)