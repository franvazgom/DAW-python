from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fechas de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fechas de actualización')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    