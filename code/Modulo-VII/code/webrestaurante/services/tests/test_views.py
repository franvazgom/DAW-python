from django.test import TestCase
from services.models import Service
from django.urls import reverse

class ServiceListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        n_services = 10
        for id in range(n_services):
            Service.objects.create(title= 'Servicio ' + str(id), 
            subtitle = 'Subtitulo del servicio ' + str(id), 
            content = 'Contenido del servicio ' + str(id), 
            image = 'ruta de imagen del servicio ' + str(id),
            cost=100)
    
    def test_view_url_desired_location(self):
        resp = self.client.get('/services/')
        self.assertEqual(resp.status_code, 200)
    
    def test_correct_template(self):
        resp = self.client.get('/services/')
        self.assertTemplateUsed(resp, 'services/service_list.html')

    def test_pagination_is_two(self):
        resp = self.client.get(reverse('services:service_list'))    
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(len(resp.context['service_list']) == 2)
    
    def test_pagination_remain(self):
        resp = self.client.get(reverse('services:service_list')+'?page=5')
        self.assertEqual(resp.status_code, 200)        
        self.assertTrue(len(resp.context['service_list']) == 2)
    
    def test_pagination_not_found(self):
        resp = self.client.get(reverse('services:service_list')+'?page=6')
        self.assertEqual(resp.status_code, 404)        