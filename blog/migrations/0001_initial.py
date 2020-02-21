# Generated by Django 3.0.3 on 2020-02-20 10:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=100, verbose_name='url')),
                ('description', models.TextField(blank=True, default='', max_length=1000, verbose_name='Описание')),
                ('template', models.CharField(default='blog/post_list.html', max_length=500, verbose_name='Шаблон')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
                ('paginated', models.PositiveIntegerField(default=5, verbose_name='Количество новостей на странице')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.Category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=100, verbose_name='url')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заглавие')),
                ('mini_text', models.TextField(max_length=5000, verbose_name='Краткое содержание')),
                ('text', models.TextField(max_length=10000000, verbose_name='Полное содержание')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slug', models.SlugField(max_length=100, verbose_name='url')),
                ('subtitle', models.CharField(blank=True, max_length=500, verbose_name='Подзаголовок')),
                ('edit_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата редактирования')),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/', verbose_name='Главная фотография')),
                ('template', models.CharField(default='blog/post_detail.html', max_length=500, verbose_name='Шаблон')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('viewd', models.PositiveIntegerField(default=0, verbose_name='Просмотрено')),
                ('status', models.BooleanField(default=False, verbose_name='Для зарегистрированных')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(blank=True, related_name='tag', to='blog.Tag', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Коментарий')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('moderation', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
