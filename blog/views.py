from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Tag, Post
# Create your views here.

class HomeView(View):
    def get(self, request):
        context = Category.objects.all()
        return render(request, 'blog/home.html', {'context': context})

class CategoryView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, 'blog/post_list.html', {'category': category})   


class PostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post_list.html", {'post': post})