# Generated by Django 3.0.5 on 2020-08-23 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0010_com_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='com_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_goods.Com_type'),
        ),
    ]