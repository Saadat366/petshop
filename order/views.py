from django.shortcuts import render
from .models import Client


def cart(request):
    cart_id = request.session["cart"]
    cart = Client.objects.get(id=cart_id)
    return render(request, "order/cart.html", {"cart": cart})