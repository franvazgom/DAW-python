from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm, ContactForm2
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST

@require_POST
def get_cities(request):
    country = request.POST.get('country', '')
    if country == 'México':
        cities = ['Ciudad de México', 'Guadalajara', 'Monterrey']
    elif country == 'USA':
        cities = ['Nueva York', 'Los Ángeles', 'Chicago', 'Orlando']
    elif country == 'Canada':
        cities = ['Vancouver', 'Montreal', 'Quebec']
    else:
        cities = []
    return JsonResponse({'cities':cities})

@require_http_methods(['GET'])
def get_countries(request):
    countries = ['México', 'USA', 'Canada']
    return JsonResponse({'countries':countries})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            print("--------------------------------------------")
            print(name, email, content)
            # dominio = 'gmail.com'
            # if dominio not in email:
            #     form.add_error('email', 'El dominio debe ser de Gmail')
            #     return render(request, 'contact/contact.html', {'form':form})            
            # return HttpResponseRedirect('/contact/thanks/')
            return HttpResponseRedirect(reverse_lazy('contact:thanks'))
        else:
            print("Forumlario inválido")
    else: # Método es GET
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form':form})

def thanks(request):
    return render(request, 'contact/thanks.html')