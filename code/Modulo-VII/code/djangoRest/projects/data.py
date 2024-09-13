import json
from projects.models import Project

class Data:
    def get_test_data(self):
        res = {'nombre':'Juan Pérez'}
        return json.dumps(res)
    
    def get_suma(self, num1, num2):
        suma = num1 + num2
        res = {'suma':suma}
        return json.dumps(res)
    
    def get_projects(self, parametros=None):
        projects = Project.objects.all()
        if parametros:
            if 'title' in parametros:
                projects = projects.filter(title__contains = parametros['title'])
            if 'description' in parametros:
                projects = projects.filter(description__contains = parametros['description'])
        return projects
