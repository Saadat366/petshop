from django.shortcuts import render, HttpResponse, \
    redirect
from product.views import products

def home(request):
    return redirect("products") # есть 3 спрособа redirect