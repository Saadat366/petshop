from django.contrib import admin
from product.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    fields = ["name", "user", "category", "price", "in_stock", "exist"] # на уровне товара
    list_display = [field.name for field in Product._meta.get_fields()[1:]]
    # list_display_links = ["id", "name"] - обозначение ссылки
    list_editable = ["in_stock"] # лучше использовать на важные поля, например: цена
    # search_fields = ["name", "user__username"]
    # list_filter = ["category", "price"]
    readonly_fields = ["name", "user", "price", "was_bought"]
    # list_per_page = 10

# admin.site.register(Product, ProductAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["id", "name"]
    list_editable = ["name"]