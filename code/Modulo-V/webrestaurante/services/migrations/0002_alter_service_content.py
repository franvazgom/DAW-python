# Generated by Django 5.0.6 on 2024-07-23 02:04

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]
