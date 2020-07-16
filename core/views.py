from django.shortcuts import render, HttpResponse, \
    redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from product.views import products
from core.forms import RegistrationForm

def home(request):
    return redirect("products") # есть 3 спрособа redirect

def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    context = {}
    if "login" in request.POST:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(home)
    context["form"] = AuthenticationForm()
    return render(request, "core/login.html", context)

def logout(request):
    auth.logout(request)
    return redirect(home)

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {}
    context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)