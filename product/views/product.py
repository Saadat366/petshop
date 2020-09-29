from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from product.models import Product


def product_def(request, id):
    context = {}
    try:
        context["product"] = Product.objects.get(id=id)
    except:
        context["type"] = "danger"
        context["message"] = "Такого товара нет"
        return render(request, "core/message.html", context)
    return render(request, "product/product.html", context)

# class ProductView(TemplateView):
#     template_name = "core/test.html"

#     def get_context_data(self, **kwargs): pk=1
#         context = {}
#         # context = super(ProductView, self).get_context_data(**kwargs)
#         pk = self.kwargs["pk"]
#         product = Product.objects.get(id=pk)
#         context["product"] = product
#         return context

class ProductDetailView(DetailView):
    template_name = "product/product.html"
    model = Product