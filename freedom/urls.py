from django.urls import path
from . import views

app_name = 'freedom'

urlpatterns = [
    path('', views.home, name='home'), 
    path('submit/', views.submit_freedom_post, name='submit_post'),
    path('my-posts/', views.my_freedom_posts, name='my_freedom_posts'),
    path('all-posts/', views.all_freedom_posts, name='all_freedom_posts'),
    path('admin-posts/', views.admin_freedom_posts, name='admin_freedom_posts'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
path('upvote/<int:pk>/', views.upvote_post, name='upvote_post'),

]
