from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Tag, Post
# Create your views here.

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        posts = Post.objects.all()
        print(categories, posts)
        return render(request, 'blog/home.html', {'categories': categories, 'posts': posts})

class CategoryView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, 'blog/post_list.html', {'category': category})   

class PostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post_list.html", {'post': post})