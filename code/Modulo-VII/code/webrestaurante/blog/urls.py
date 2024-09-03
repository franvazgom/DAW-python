from django.urls import path
from blog import views

blog_urlpatterns = ([
    path('', views.blog, name='post'),
    path('category/<int:category_id>', views.category, name='category'),
], 'blog')