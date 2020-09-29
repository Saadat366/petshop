from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from product.forms import *

@user_passes_test(lambda user: user.is_staff)
def category_create(request):
    context = {}
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect("category", pk=category.id)

    form = CategoryCreateForm()
    context["form"] = form
    return render(request, "product/category_create.html", context)
        