from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from product.models import Product

def products(request):
    if "key_word" in request.GET:
        key = request.GET.get("key_word")
        products = Product.objects.filter(
            Q(exist=True),
            Q(name__contains=key) |
            Q(description__contains=key) |
            Q(category__name__contains=key)
            )
    else:
        products = Product.objects.filter(exist=True)
    return render(request, "product/products.html", {"products": products})