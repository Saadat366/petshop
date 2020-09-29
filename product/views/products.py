from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from product.models import Product

def products(request):
    if "key_word" in request.GET:
        key = request.GET.get("key_word")
        object_list = Product.objects.filter(
            Q(exist=True),
            Q(name__contains=key) |
            Q(description__contains=key) |
            Q(category__name__contains=key)
            )
    else:
        object_list = Product.objects.filter(exist=True)
    return render(request, "product/products.html", {"object_list": object_list})

class ProductList(ListView):
    model = Product
    template_name = "product/products.html"
    queryset = Product.objects.filter(exist=True)