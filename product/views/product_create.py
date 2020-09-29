from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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
    return render(request, "product/product_create.html", context)

class ProductCreateView(LoginRequiredMixin ,CreateView):
    login_url = "/login"
    model = Product
    form = ProductForm
    fields = ["name", "category", "image", "description", "price"]
    template_name = "product/product_create.html"
    success_url = reverse_lazy("products")