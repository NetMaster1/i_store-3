# Generated by Django 3.0.5 on 2020-06-17 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Cart',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='photos')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('display', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3)),
                ('hdd', models.IntegerField(default=0)),
                ('ram', models.IntegerField(default=0)),
                ('colour', models.CharField(blank=True, default='Black', max_length=250)),
                ('camera_1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('camera_2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('front_camera', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('processor_frequency', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('processor_core', models.IntegerField(default=0)),
                ('battery', models.CharField(blank=True, max_length=5)),
                ('image', models.ImageField(blank=True, upload_to='photos')),
                ('image_1', models.ImageField(blank=True, upload_to='photos')),
                ('image_2', models.ImageField(blank=True, upload_to='photos')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(blank=True, default='Samsung', on_delete=django.db.models.deletion.DO_NOTHING, to='app_goods.Brand')),
                ('category', models.ForeignKey(blank=True, default='Smartphones', on_delete=django.db.models.deletion.DO_NOTHING, to='app_goods.Category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('model_name',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='photos')),
                ('slug', models.SlugField(max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_goods.Cart')),
            ],
            options={
                'db_table': 'CartItem',
            },
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='photos')),
                ('stock', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.ManyToManyField(to='app_goods.Product')),
            ],
            options={
                'verbose_name': 'accessory',
                'verbose_name_plural': 'accessories',
                'ordering': ('name',),
            },
        ),
    ]
