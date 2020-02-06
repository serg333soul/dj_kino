from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.CategoryView.as_view()),
    path('', views.HomeView.as_view())
]