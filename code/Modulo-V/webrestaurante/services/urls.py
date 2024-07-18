from django.urls import path
from services import views

services_urlpatterns = ([
    path('', views.service_list, name='service_list'),    
], 'services')