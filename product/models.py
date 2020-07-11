from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name = "Наименование")
    category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        related_name="product",
        null=True,
        blank=True,
        verbose_name="Категория"
    )
    image = models.ImageField(null=True, blank=True, upload_to="product_image", verbose_name="Изображение товара")
    description = models.TextField(null=True, blank=True, verbose_name = "Описание")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = "Цена")
    was_bought = models.IntegerField(default=0, verbose_name = "Количество продаж") 
    in_stock = models.BooleanField(default=False, verbose_name = "В наличии")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"
