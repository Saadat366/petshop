from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.forms import ProductForm
from product.models import Product


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