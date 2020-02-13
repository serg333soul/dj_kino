from django.db import models
from datetime import datetime
from mptt.fields import TreeForeignKey

# Create your models here.
class Category(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)
    description = models.TextField('Описание', max_length=1000, default='', blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name = 'Родительская категория',
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = 'children'
    )
    template = models.Charfield('Шаблон', max_length=500, default='blog/post_list.html')
    published = models.BooleanField('Отображать?', default=True)
    paginated = models.PositiveIntegerField('Количество новостей на странице', default=5)
    sort = models.PositiveIntegerField('Порядок', default=0)

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