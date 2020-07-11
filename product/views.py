from django.shortcuts import render
from product.models import *

def products(request):
    products = Product.objects.filter(in_stock=True)
    return render(request, "product/products.html", {"products": products})