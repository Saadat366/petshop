from django.shortcuts import redirect
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import PasswordChangeForm


# @login_required
# def change_pw(request):
#     if request.method == "POST":
#         form = PasswordChangeForm(request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)

#     return redirect("profile", pk=user.id)

@require_http_methods(["POST"])
def change_pw(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
    
    return redirect("login")