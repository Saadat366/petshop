from django.shortcuts import render, HttpResponse, \
    redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from product.views import products
from core.forms import RegistrationForm
from product.models import Product

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

@login_required(login_url="/login/")
def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["products"] = Product.objects.filter(user=context["user"])
    return render(request, "core/profile.html", context)

def sellers(request):
    sellers = User.objects.exclude(product=None)
    context = {"sellers": sellers}
    return render(request, "core/sellers.html", context)