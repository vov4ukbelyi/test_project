from django.contrib import admin
from .models import Category, Product



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['created_at']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)