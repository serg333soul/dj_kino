from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import View
from .models import Category, Tag, Post, Comment

class PostListView(View):
    '''Вывод статьей категории'''
    def get_queryset(self):
        return Post.objects.filter(published_date_lte=datetime.now(), published=True)
    
    def get(self, request, category_slug=None, slug=None):
        category_list = Category.objects.filter(published=True)
        if category_slug is not None:
             posts = self.get_queryset().filter(category__slug=category_slug,
                                                category__published=True
                                                )
        elif slug is not None:
            posts = self.get_queryset().filter(tags__slug=slug, tags__published=True)
        else:
            posts = self.get_queryset()
        if posts.exists():
            template = 'blog/post_list.html'
        return render(request, template, {
            'post_list': posts,
            'catigories': category_list
        })    

class HomeView(View):
    '''Home page'''
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request, 'blog/post_list.html', {'categories': category_list, 'post_list': post_list})
        
class TagDetailView(View):
    def get(self, request, slug):
        tag_list = Post.objects.filter(tags__slug=slug, tags__published=True)
        print('---------------------', tag_list)
        return render(request, 'blog/tag_detail.html', {'tag_list': tag_list})

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


