from django.shortcuts import render, HttpResponse, \
    redirect
from django.contrib.auth.forms import AuthenticationForm, \
    UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from product.views import products
from core.forms import *
from product.models import Product

def home(request):
    return redirect("products") # есть 3 спрособа redirect

def user_not_authenticated(user):
    return not user.is_authenticated

@user_passes_test(user_not_authenticated)
def login(request):
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

@user_passes_test(user_not_authenticated)
def registration(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if form.is_valid():
            form.save()
            return redirect(home)

    context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)

def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["products"] = Product.objects.filter(user=context["user"])
    context["pw_change_form"] = ChangePasswordForm()
    return render(request, "core/profile.html", context)

def sellers(request):
    sellers = User.objects.exclude(product=None)
    context = {"sellers": sellers}
    return render(request, "core/sellers.html", context)

@require_http_methods(["POST"])
def change_pw(request):
    user = request.user
    password_1 = request.POST.get("password_1")
    password_2 = request.POST.get("password_2")
    if password_1 == password_2:
        user.set_password(password_1)
        user.save()
    return redirect("profile", pk=user.id)