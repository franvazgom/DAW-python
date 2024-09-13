from rest_framework.test import APITestCase
import json
from projects.models import Project

class ProjectServiceTest(APITestCase):
    def setUp(self):
        self.url = '/projectService/'
        for i in range(5):
            Project.objects.create(title=f"Proyecto {i}",
                                   description = f"Descripcion {i}")
    
    def test_without_parameters(self):
        data = {
            'parametros':{}
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.data['resultado'])
        self.assertEqual(len(res), 5)
    
    def test_with_parameters(self):
        data = {
            'parametros':{'title':'Proyecto 2'}
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.data['resultado'])
        self.assertEqual(res[0]["description"], "Descripcion 2")