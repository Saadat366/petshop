from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name = "Наименование"
        )
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="product",
        verbose_name="Пользователь"
    )
    category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="product",
        verbose_name="Категория"
    )
    image = models.ImageField(
        null=True, blank=True,
        upload_to="product_image",
        verbose_name="Изображение товара",
        default="static/no-image.png"
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name = "Описание"
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name="Цена"
    )
    was_bought = models.IntegerField(
        default=0,
        verbose_name="Количество продаж"
    ) 
    in_stock = models.BooleanField(
        default=True,
        verbose_name="В наличии"
    )
    exist = models.BooleanField(
        default=True,
        verbose_name="Отображать на сайте")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"