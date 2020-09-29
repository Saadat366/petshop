from django.db import models
from product.models import Product

class Client(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Заказчик"
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Номер телефона"
    )
    address = models.CharField(
        max_length=255,
        verbose_name = "Адрес"
    )

    class Meta:
        verbose_name = "заказчик"
        verbose_name_plural = "Заказчики"

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(
        to="Client",
        on_delete=models.CASCADE,
        related_name="order"
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="order",
        verbose_name="Товар"
    )
    product_count = models.PositiveSmallIntegerField(
        verbose_name="Количество"
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время заказа"
    )
    
    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"