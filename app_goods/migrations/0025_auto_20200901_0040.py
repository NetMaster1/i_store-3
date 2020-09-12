# Generated by Django 3.0.5 on 2020-08-31 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0024_biometrics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biometrics',
            options={'ordering': ('name',), 'verbose_name': 'biometrics', 'verbose_name_plural': 'biometrics'},
        ),
        migrations.AddField(
            model_name='product',
            name='biometrics',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_goods.Biometrics'),
        ),
    ]
