from django.shortcuts import render
from product.models import *

def products(request):
    products = Product.objects.filter(in_stock=True)
    return render(request, "product/products.html", {"products": products})

def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)