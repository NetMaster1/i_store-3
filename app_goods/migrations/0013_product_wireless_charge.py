# Generated by Django 3.0.5 on 2020-08-24 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0012_product_nfc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wireless_charge',
            field=models.BooleanField(default=False),
        ),
    ]