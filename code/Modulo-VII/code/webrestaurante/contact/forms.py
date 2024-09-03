from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Escribe tu nombre'
            }
        ),
        min_length=3,
        max_length=100
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Escribe tu email'
            }
        ),
        min_length=3,
        max_length=100
    )
    content = forms.CharField(
        label='Contenido',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'rows':'4',
                'placeholder':'Escribe tu mensaje'
            }
        ),
        min_length=3,
        max_length=100
    )

    #Validación exclusiva para el campo de email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        dominio = 'gmail.com'
        if dominio not in email:
            raise forms.ValidationError(f'El correo debe ser {dominio}')
        return email

    # Validación general
    def clean(self):
        cleaned_data = super().clean()
        name =  cleaned_data.get('name')
        email = cleaned_data.get('email')
        if name and email:
            if name in email:
                raise forms.ValidationError(
                    'El nombre del usuario no puede aparecer en el correo'
                )
        return cleaned_data

class ContactForm2(forms.Form):
    name = forms.CharField(min_length=5)
    email = forms.EmailField()
    content = forms.CharField()

    #Validación exclusiva para el campo de email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        dominio = 'gmail.com'
        if dominio not in email:
            raise forms.ValidationError(f'El correo debe ser {dominio}')
        return email

    # Validación general
    def clean(self):
        cleaned_data = super().clean()
        name =  cleaned_data.get('name')
        email = cleaned_data.get('email')
        if name and email:
            if name in email:
                raise forms.ValidationError(
                    'El nombre del usuario no puede aparecer en el correo'
                )
        return cleaned_data