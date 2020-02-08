from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('<slug:slug>/', views.PostView.as_view(), name='post'),
    path('', views.HomeView.as_view()),
]