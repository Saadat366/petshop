# Generated by Django 3.0.8 on 2020-07-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Изображение товара'),
        ),
    ]
