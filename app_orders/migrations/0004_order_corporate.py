# Generated by Django 3.0.5 on 2020-09-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0003_auto_20200905_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='corporate',
            field=models.BooleanField(default=False),
        ),
    ]
