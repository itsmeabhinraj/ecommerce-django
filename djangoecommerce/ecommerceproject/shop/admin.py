from django.contrib import admin

from .models import Product


# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']


# admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price','stock', 'img')
    list_editable = ['desc', 'stock','price']
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
