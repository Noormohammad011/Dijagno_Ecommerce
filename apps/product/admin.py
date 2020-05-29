from django.contrib import admin
from . models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin): 
    list_filter  = ['status']
    list_display = ['title', 'parent', 'status']


class ProductAdmin(admin.ModelAdmin): 
    list_filter  = ['status']
    list_display = ['title', 'parent', 'status']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
