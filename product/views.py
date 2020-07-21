from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, \
    user_passes_test
from product.models import *
from product.forms import ProductForm

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

def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)

@login_required(login_url="login")
def product_create(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
            new_product.save()
            context["products"] = Product.objects.filter(in_stock=True, exist=True)
            context["message"] = "Товар добален"
            return render(request, "product/products.html", context)
    context["form"] = ProductForm()
    return render(request, "product/form.html", context)

@login_required(login_url="login")
def product_edit(request, id):
    product = Product.objects.get(id=id)
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context["product"] = Product.objects.get(id=id)
            context["message"] = "Редактирование прошло успешно"
            return render(request, "product/product.html", context)

    context["form"] = ProductForm(instance=product)
    return render(request, "product/form.html", context)