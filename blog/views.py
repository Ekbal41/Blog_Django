from django.shortcuts import render

from .models import Post, Category

# Create your views here.

def index(request):
    first_posts = Post.objects.all()[0:1]
    posts = Post.objects.all()[1:]
    
    context ={
        'first_posts': first_posts,
        'posts': posts,
    }
    
    return render(request, 'blog/index.html', context)

def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context ={
       
        'post': post,
    }
    return render(request, 'blog/blog-detail.html', context)

def category(request, slug):
    posts = Post.objects.filter(category__slug=slug)
    context ={
       
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def blog_archive(request, year, month):
    posts = Post.objects.filter(created_on__year=year, created_on__month=month)
    context ={
       
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)