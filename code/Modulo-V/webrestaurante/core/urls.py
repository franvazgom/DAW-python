from django.urls import path
from core import views as views_core

core_urlpatterns = ([
    path('', views_core.home, name='home'),
    path('about/', views_core.about, name='about'),
    path('visit-us/', views_core.store , name='visit-us'),
], 'core')