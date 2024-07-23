from django.shortcuts import render, HttpResponseRedirect
from services.models import Service
from .forms import ServiceForm
from django.contrib.admin.views.decorators import staff_member_required

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services':services})

@staff_member_required
def create(request):
    # if not request.user.is_staff:
    #     return HttpResponseRedirect('/')    
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/services')        
    else: #Método GET
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form':form})

@staff_member_required
def update(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/services')        
    else: #Método GET
        form = ServiceForm(instance=service)
    return render(request, 'services/service_update_form.html', {'form':form})

@staff_member_required
def delete(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    return HttpResponseRedirect('/services')        
    
