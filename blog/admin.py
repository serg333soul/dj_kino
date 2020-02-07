from django.contrib import admin

# Register your models here.
from . models import Category
from . models import Tag

admin.site.register(Category)
admin.site.register(Tag)