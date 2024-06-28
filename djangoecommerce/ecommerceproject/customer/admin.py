from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'quantity', 'price')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
