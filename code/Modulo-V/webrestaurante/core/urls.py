from django.urls import path
from core import views as views_core
from django.contrib.auth import views as auth_views

core_urlpatterns = ([
    path('', views_core.home, name='home'),
    path('about/', views_core.about, name='about'),
    path('visit-us/', views_core.store , name='visit-us'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
], 'core')