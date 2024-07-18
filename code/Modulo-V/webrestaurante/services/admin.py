from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'subtitle', 'created',)
    search_fields = ('title', 'subtitle')
    list_filter = ('title', 'subtitle')

admin.site.register(Service, ServiceAdmin)