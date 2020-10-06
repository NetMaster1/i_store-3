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
        ordering = ('name',)  # sorting by name
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    # def get_url(self):
    #     return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'color'
        verbose_name_plural = 'color'

    def __str__(self):
        return self.name

class Operator(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'operator'
        verbose_name_plural = 'operators'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name

class Com_type(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'com_type'
        verbose_name_plural = 'com_types'

    def __str__(self):
        return self.name

class Security_class(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'security_class'
        verbose_name_plural = 'security_class'

    def __str__(self):
        return self.name

class Tarif(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    operator = models.ForeignKey(Operator, null=True, blank=True, on_delete=models.DO_NOTHING)
    line_rental = models.IntegerField(default=0)
    free_min = models.IntegerField(default=0)
    free_gb = models.IntegerField(default=0)
    home_tax = models.IntegerField(default=0)
    out_tax = models.IntegerField(default=0)
    stationary_tax = models.IntegerField(default=0)
    gb_tax = models.IntegerField(default=0)
    sms = models.IntegerField(default=0)
    description = models.TextField(blank=True)
  
    class Meta:
        ordering = ('name',)
        verbose_name = 'tarif'
        verbose_name_plural = 'tarifs'

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'sensor'
        verbose_name_plural = 'sensors'

    def __str__(self):
        return self.name


class Body_material(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'body_material'
        verbose_name_plural = 'body_materials'

    def __str__(self):
        return self.name


class Lace_material(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'lace_material'
        verbose_name_plural = 'lace_materials'

    def __str__(self):
        return self.name


class Biometrics(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'biometrics'
        verbose_name_plural = 'biometrics'

    def __str__(self):
        return self.name

class Product(models.Model):
    model_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, default="Smartphones", blank=True, on_delete=models.DO_NOTHING)
    operator = models.ForeignKey(Operator, null=True, blank=True, on_delete=models.DO_NOTHING)
    sim_cards = models.CharField(max_length=250, blank=True)
    os = models.CharField(max_length=250, blank=True)
    tarif = models.ForeignKey(Tarif, null=True, blank=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    display = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)
    display_color = models.BooleanField(default=True)
    hdd = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    camera_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    camera_2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    front_camera = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    video = models.CharField(max_length=50, blank=True)
    processor_name = models.CharField(max_length=250, blank=True)
    processor_frequency = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    processor_core = models.IntegerField(default=0)
    sensor = models.ManyToManyField(Sensor, blank=True)
    security_class = models.ManyToManyField(Security_class, blank=True)
    com_type = models.ManyToManyField(Com_type, blank=True)
    body_material = models.ForeignKey(Body_material, null=True, blank=True, on_delete=models.DO_NOTHING)
    lace_material = models.ForeignKey(Lace_material, null=True, blank=True, on_delete=models.DO_NOTHING)
    biometrics = models.ForeignKey(Biometrics, null=True, blank=True, on_delete=models.DO_NOTHING)
    wireless_charge = models.BooleanField(default=False)
    nav = models.BooleanField(default=True)
    additional_features = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='photos', blank=True)
    image_1 = models.ImageField(upload_to='photos', blank=True)
    image_2 = models.ImageField(upload_to='photos', blank=True)
    stock = models.IntegerField()
    sales = models.BooleanField(default=False)
    bestsellers = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('model_name',)  # sorting by name
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        #     #return reverse('product_detail', args=[self.category.slug, self.slug])
        return reverse('product_detail', args=[self.id])

    def __str__(self):
        return self.model_name


class Accessory(models.Model):
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    link = models.ManyToManyField(Product)
    image = models.ImageField(upload_to='photos', blank=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'accessory'
        verbose_name_plural = 'accessories'
    def get_url(self):
        #return reverse('product_detail', args=[self.category.slug, self.slug])
        return reverse('accessory_detail', args=[self.id])

    def __str__(self):
        return self.name

    # CartTables
# ====================================================


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id
    #def __unicode__(self):
    #    return "Cart id: %s" %(self.id)

class CartItem(models.Model):
    brand = models.CharField(max_length=100, blank=True)
    product = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos', blank=True)
    slug = models.SlugField(max_length=100, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.price * self.quantity

    def __str__(self):
        return self.product

    def get_url(self):
        if Accessory.objects.filter(slug=self.slug).exists():
            accessory = Accessory.objects.get(slug=self.slug)
            return reverse('accessory_detail', args=[accessory.id])
        else:
            product = Product.objects.get(slug=self.slug)
            return reverse('product_detail', args=[product.id])
