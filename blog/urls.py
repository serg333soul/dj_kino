from django.urls import path
from . import views

urlpatterns = [
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag'),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name='detail_post'),
    path('<slug:category_name>/', views.CategoryView.as_view(), name='category'),
    path('', views.HomeView.as_view()),
]