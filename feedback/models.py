from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="feedback",
    )
    phone_number = models.CharField(
        max_length=200,
        null=True, blank=True,
        verbose_name="Номер телефона"
    )
    email = models.EmailField(
        max_length=255,
        null=True, blank=True,
        verbose_name="e-mail"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Тема"
    )
    text = models.TextField(
        null=True, blank=True,
        verbose_name="Текст обращения",
    )
    image = models.ImageField(
        upload_to="feedback",
        null=True, blank=True,
        verbose_name="Приложенное изображение"
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    answer = models.TextField(
        null=True,blank=True,
        verbose_name="Ответ на отзыв"
    )

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Формы обратной связи"