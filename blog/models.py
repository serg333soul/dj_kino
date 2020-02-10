from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'    

class Post(models.Model):
    title = models.CharField('Заглавие', max_length=500)
    mini_text = models.TextField('Описание')
    text = models.TextField('Текст')
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'    
    
class Comment(models.Model):
    text = models.TextField('Коментарий')
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    moderation = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'