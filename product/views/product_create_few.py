from django.shortcuts import render
from django.forms import formset_factory
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from product.forms import ProductForm
from product.models.product import Product


def product_create_few(request):
    ProductFormSet = modelformset_factory(
        Product,
        form=ProductForm,
        extra=1
    )
    context = {}
    if request.method == "POST":
        formset = ProductFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect(reverse("home"))
    context["formset"] = ProductFormSet(queryset=Product.objects.none)
    return render(request, "product/product_create_few.html", context)