from django.shortcuts import redirect


def home(request):
    return redirect("products") # есть 3 спрособа redirect