from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import FeedbackForm

@login_required(login_url="login")
@require_POST
def feedback(request):
    context = {}
    form = FeedbackForm(request.POST, request.FILES)
    if form.is_valid():
        feedback = form.save()
        context["message"] = "Ваш отзыв принят! Спасибо!"
        context["type"] = "success"
        return render(request, "core/message.html", context)
    context["message"] = "Форма заполнена неверно"
    context["type"] = "warning"
    return render (request, "core/message.html", context)
