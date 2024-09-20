# Generated by Django 5.1 on 2024-09-20 01:45

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=200, verbose_name='DIrección')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Total')),
                ('correo', models.EmailField(max_length=254, verbose_name='Email')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['-fecha'],
                'permissions': [('can_edit_order', 'can edit order')],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtítutlo')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imágen')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['-updated'],
            },
        ),
    ]
