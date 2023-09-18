from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:pk>/', user_profile, name='profile'),
    path('profile_edit/<int:pk>/', profile_edit, name='profile_edit'),
    path('article/<int:pk>/', article_view, name='article'),
    path('article/<int:pk>/update', article_update, name='article_update'),
    path('article/<int:pk>/delete', article_delete, name='article_delete'),
    path('my_posts/', my_posts, name='my_posts'),
    path('category/<int:pk>/', category, name='category'),
    path('add_article/', add_article, name='add_article'),
    path('comment_delete/<int:pk>/', comment_delete, name='comment_delete'),
]