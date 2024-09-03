from django.forms import ModelForm, TextInput, Textarea
from services.models import Service
from django_ckeditor_5.widgets import CKEditor5Widget

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
        