# Generated by Django 3.0.5 on 2020-08-31 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0021_product_os'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
