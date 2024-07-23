from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    subtitle = models.CharField(max_length=100, verbose_name='Subtítutlo')
    content = CKEditor5Field('Contenido', config_name='extends', blank=True, null=True)
    image = models.ImageField(verbose_name='Imágen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-updated']
    
    def __str__(self):
        return self.title
