from django.contrib import admin
from .models import Service, Order

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'subtitle', 'created',)
    search_fields = ('title', 'subtitle')
    list_filter = ('title', 'subtitle')

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    list_display = ('nombre', 'total',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)