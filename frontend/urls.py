from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('datasets/', views.datasets, name='datasets'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('datasets/<int:id>/', views.dataset_detail, name='dataset_detail'),
    path('datasets/create/', views.dataset_create, name='dataset_create'),
    path('categories/', views.categories, name='categories'),
    path('profile/', views.profile, name='profile'),
]