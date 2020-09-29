from django.contrib import admin
from .models import *

class OrderInLine(admin.TabularInline):
    model = Order

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    inlines = [OrderInLine]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["client", "product", "product_count", "order_date"]
    readonly_fields = ["client", "product", "product_count", "order_date"]