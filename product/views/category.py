from django.shortcuts import render
from product.models import Product


def category(request, pk):
    context = {}
    context["object_list"] = Product.objects.filter(
        category__id=pk,
        in_stock=True,
        exist=True)
    context["category_pk"] = pk
    return render(request, "product/products.html", context)