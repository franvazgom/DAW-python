from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse_lazy

def contact(request):
    print(request.method)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            print(name, email, content)
            dominio = 'gmail.com'
            if dominio not in email:
                form.add_error('email', 'El dominio debe ser de Gmail')
                return render(request, 'contact/contact.html', {'form':form})            
            # return HttpResponseRedirect('/contact/thanks/')
            return HttpResponseRedirect(reverse_lazy('contact:thanks'))
    else: # Método es GET
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form':form})

def thanks(request):
    return render(request, 'contact/thanks.html')