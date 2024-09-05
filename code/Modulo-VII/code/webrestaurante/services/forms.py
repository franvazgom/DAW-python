from django.forms import ModelForm, TextInput, Textarea, EmailInput
from services.models import Service, Order
from django_ckeditor_5.widgets import CKEditor5Widget

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['nombre', 'direccion', 'total', 'correo']
    
        widgets = {
            'nombre':TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'direccion':TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
            'correo':EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'total':TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        }

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title':TextInput(attrs={'class':'form-control','placeholder':'Título'}),
            'subtitle':TextInput(attrs={'class':'form-control','placeholder':'Subtítutlo'}),
            'content':CKEditor5Widget(config_name='extends'),
        }
    
    def clean(self):
        super(ServiceForm,self).clean()
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._errors['title'] = self.error_class(['Mínimo 5 caracteres'])
        return self.cleaned_data
        