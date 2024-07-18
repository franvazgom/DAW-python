from django.shortcuts import render
from services.models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services':services})