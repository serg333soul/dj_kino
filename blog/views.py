from django.shortcuts import render
from django.views.generic.base import View
from . models import Category
# Create your views here.

class HomeView(View):

    def get(self, request):
        context = Category.objects.all()
        return render(request, 'blog/home.html', {'context': context})
        