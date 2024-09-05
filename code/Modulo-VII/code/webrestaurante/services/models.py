from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Order(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.CharField(max_length=200, verbose_name="DIrección")
    total = models.DecimalField(verbose_name='Total', max_digits=8, decimal_places=2)
    correo = models.EmailField(verbose_name='Email')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha']

    def __str__(self):
        return str(self.id)

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    subtitle = models.CharField(max_length=100, verbose_name='Subtítutlo')
    content = CKEditor5Field('Contenido', config_name='extends', blank=True, null=True)
    image = models.ImageField(verbose_name='Imágen', upload_to='services')
    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-updated']
    
    def __str__(self):
        return self.title
