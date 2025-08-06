from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:blog_id>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),
    path('register/', views.register, name='register'),
    path('detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Added detail view for individual blog posts
    path('about/', views.about, name='about'),  # Added about page
    path('services/', views.services, name='services'),  # Added services page
    path('contact/', views.contact, name='contact'),  # Added contact page
]