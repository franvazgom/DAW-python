from django.shortcuts import render
from .models import Project

def project(request):
    projects = Project.objects.all()
    return render(request, 'project/project.html', {'projects':projects})
