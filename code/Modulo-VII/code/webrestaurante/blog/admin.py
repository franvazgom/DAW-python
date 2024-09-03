from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'author_name', 'published', 'categories_names',)
    search_fields = ('title', 'author__first_name', 'categories__name',)
    date_hierarchy = 'published'
    list_filter = ('categories__name', 'author__first_name', 'published',)

    def author_name(self, obj):        
        return obj.author.first_name + " " + obj.author.last_name

    def categories_names(self, obj):
        return ", ".join([category.name for category in obj.categories.all().order_by('name')])
        
    categories_names.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


