from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import View
from .models import Category, Tag, Post, Comment


class HomeView(View):
    '''Home page'''
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request, 'blog/post_list.html', {'categories': category_list, 'post_list': post_list})

class TagDetailView(View):
    pass

class PostDetailView(View):
    '''Вывод полной статьи'''
    def get(self, request, category, slug):
        category_list = Category.objects.all() 
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post_id=post.id)
        
        context = {
            'categories': category_list, 
            'post': post, 
            'comments': comments,
        }

        print('_____________________________', comments)
        return render(request, post.template, context)

class CategoryView(View):
    '''Вывод статей категории'''
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        print('_____________________', category)
        posts = Post.objects.filter(category_id=category.id)
        return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})

           
