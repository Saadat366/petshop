# Generated by Django 3.0.8 on 2020-07-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200721_0316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterField(
            model_name='product',
            name='exist',
            field=models.BooleanField(default=True, verbose_name='Отображать на сайте'),
        ),
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True, verbose_name='В наличии'),
        ),
    ]