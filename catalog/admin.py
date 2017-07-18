# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    
    # o __name permite que eu pesquise usando o valor do atributo, no caso, o nome da categoria
    search_fields = ['name', 'category__name','slug']
    
    list_filter = ['created', 'modified']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)