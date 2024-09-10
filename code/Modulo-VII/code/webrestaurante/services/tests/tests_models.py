from django.test import TestCase
from services.models import Service

class ServiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Service.objects.create(
            title = 'Servicio 1',
            subtitle = 'Subtitulo 1',
            content = 'Contenido 1',
            image = 'ruta de imagen',
            cost = 34.56
        )
    
    def test_db_not_empty(self):
        services = Service.objects.all()
        self.assertIs(len(services) > 0, True)
    
    def test_name_label(self):
        service = Service.objects.get(id=1)
        label = service._meta.get_field('title').verbose_name
        self.assertEqual(label, 'Título')
    
    def test_title_max_length(self):
        service = Service.objects.get(id=1)
        length = service._meta.get_field('title').max_length
        self.assertEqual(length, 100)
