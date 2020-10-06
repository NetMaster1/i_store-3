# Generated by Django 3.0.5 on 2020-08-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0009_auto_20200823_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Com_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'com_type',
                'verbose_name_plural': 'com_types',
                'ordering': ('name',),
            },
        ),
    ]