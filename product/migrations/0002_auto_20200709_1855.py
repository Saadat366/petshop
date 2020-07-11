# Generated by Django 3.0.8 on 2020-07-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='was_bougth',
        ),
        migrations.AddField(
            model_name='product',
            name='was_bought',
            field=models.IntegerField(default=0, verbose_name='Количество продаж'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False, verbose_name='В наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена'),
        ),
    ]
