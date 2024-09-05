from django.shortcuts import render, HttpResponseRedirect
from services.models import Service
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import ServiceForm, OrderForm
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy

class OrderSuccess(TemplateView):
    template_name = 'services/order_success.html'

class ServiceCreateOrder(CreateView):
    form_class = OrderForm
    template_name = 'services/order_client.html'
    success_url = reverse_lazy('services:success_order')

    def get_initial(self):
        initial = super().get_initial()
        initial['total'] = self.request.session.get('total_order')
        return initial

def _create_dict(data_order):
    res = {}
    data_order = data_order[:-1]
    products = data_order.split('|')
    for product in products:
        detail = product.split('-')
        res[detail[0]] = int(detail[1])
    return res

def order_request(request):
    order = list()
    if request.method == 'POST':
        data_order = request.POST['data_order']
        products = _create_dict(data_order)
        total = 0
        for key, qty in products.items():
            product = {} 
            service = Service.objects.get(pk=key)
            product['id'] = service.id
            product['descripcion'] = service.title            
            product['cantidad'] = qty
            product['precio'] = str(service.cost)
            product['subtotal'] =  str(qty * service.cost)
            total += qty * service.cost
            order.append(product)
        total = str(total)
        request.session['total_order'] = total
        request.session['detail_order'] = order
    return render(request, 'services/detail_order.html', {'order':order, 'total':total})

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
    
