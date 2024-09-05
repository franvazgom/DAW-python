from django.urls import path
from services import views
from services.views import ServiceCreateOrder, OrderSuccess

services_urlpatterns = ([
    path('', views.service_list, name='service_list'),    
    path('create/', views.create, name='create'), 
    path('update/<int:service_id>', views.update, name='update'), 
    path('delete/<int:service_id>', views.delete, name='delete'), 
    path('order_request/', views.order_request , name='order_request'), 
    path('order_create/', ServiceCreateOrder.as_view() , name='order_create'),
    path('success_order/', OrderSuccess.as_view() , name='success_order'),    
], 'services')