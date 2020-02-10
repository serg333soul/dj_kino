from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('post/<slug:slug>/', views.PostView.as_view(), name='post'),
    path('', views.HomeView.as_view()),
]