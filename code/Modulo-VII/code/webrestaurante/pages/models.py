from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = CKEditor5Field(verbose_name='Contenido', config_name='extends')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fechas de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fechas de actualización')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    