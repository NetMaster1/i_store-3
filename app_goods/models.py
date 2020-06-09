from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos', blank=True)
    class Meta:
        ordering = ('name',) #sorting by name
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    # def get_url(self):
    #     return reverse('product_by_category', args=[self.slug])
    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    def __str__(self):
        return self.name

class Product(models.Model):
    model_name=models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    brand=models.ForeignKey(Brand, default="Samsung", blank=True, on_delete=models.DO_NOTHING)
    category=models.ForeignKey(Category, default="Smartphones", blank=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    display=models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)
    hdd=models.IntegerField(default=0)
    ram=models.IntegerField(default=0)
    colour=models.CharField(max_length=250, default='Black', blank=True)
    camera_1=models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    camera_2=models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    front_camera=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    processor_frequency=models.DecimalField(max_digits=3, decimal_places=2, default=0)
    processor_core=models.IntegerField(default=0)
    battery=models.CharField(max_length=5, blank=True)
    image = models.ImageField(upload_to='photos', blank=True)
    image_1 = models.ImageField(upload_to='photos', blank=True)
    image_2 = models.ImageField(upload_to='photos', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('model_name',) #sorting by name
        verbose_name = 'product'
        verbose_name_plural = 'products'
    def get_url(self):
    #     #return reverse('product_detail', args=[self.category.slug, self.slug])
        return reverse('product_detail', args=[self.id])
    def __str__(self):
        return self.model_name

class Accessory(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=100, null=True, unique=True)
    link = models.ManyToManyField(Product)
    image = models.ImageField(upload_to='photos', blank=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering=('name',)
        verbose_name = 'accessory'
        verbose_name_plural = 'accessories'
    # def get_url(self):
    #     #return reverse('product_detail', args=[self.category.slug, self.slug])
    #     return reverse('accessory_detail', args=[self.id])
    def __str__(self):
        return self.name

    # CartTables
# ====================================================
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering =['date_added']
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos', blank=True)
    slug=models.SlugField(max_length=100, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price=models.DecimalField(default=0, max_digits=7, decimal_places=2)
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CartItem'
    def sub_total(self):
        return self.price * self.quantity
    def __str__(self):
        return self.product
    def get_url(self):
        if Accessory.objects.filter(slug=self.slug).exists():
            accessory=Accessory.objects.get(slug=self.slug)
            return reverse('accessory_detail', args=[accessory.id])
        else:
            product=Product.objects.get(slug=self.slug)
            return reverse('product_detail', args=[product.id])
    
    # Product Reviews
# =====================================================

# class Review(models.Model):
#     title = models.ForeignKey(Product)
#     user = models.ForeignKey(User)
#     review=models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     created = 
#     class Meta:
#         ordering = ('created',) 
#         verbose_name = 'review'
#         verbose_name_plural = 'reviews'
#     # def get_url(self):
#     #     return reverse('product_detail', args=[self.id])
#     def __str__(self):
#         return self.title