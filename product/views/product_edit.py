from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
from product.forms import ProductForm


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