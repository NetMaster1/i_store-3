# Generated by Django 3.0.5 on 2020-08-31 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0030_remove_product_internet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Internet',
        ),
    ]
