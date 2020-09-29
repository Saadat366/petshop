from django.shortcuts import redirect
from order.models import *
from product.models import Product


def add_to_cart(request, id):
    if "cart" not in request.session:
        client = Client()
        client.save()
        request.session["client"] = client.id
    else:
        client_id = request.session["client"]
        client = Client.objects.get(id=cart_id)
    product = Product.objects.get(id=id)
    order = Order(product=product, client=client)
    order.save()
    return redirect("product", id=id)