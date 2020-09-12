from django.db import models
from datetime import datetime
#from app_products.models import Product

# Create your models here.

class Order(models.Model):
    corporate = models.BooleanField(default=False) #True is for private person
    first_name=models.CharField(max_length=50, blank=True)
    last_name=models.CharField(max_length=50, blank=True)
    email=models.EmailField(blank=True)
    phone=models.CharField(max_length=50, blank=True)
    postal_code=models.CharField(max_length=50, blank=True)
    region=models.CharField(max_length=150, blank=True)
    city=models.CharField(max_length=50, blank=True)
    street=models.CharField(max_length=100, blank=True)
    building=models.CharField(max_length=50, blank=True)
    appartment = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    # updated=models.DateTimeField(default=datetime.now, blank=True)
    paid = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    class Meta:
        ordering =['created']
    def __int__(self):
        return self.id
    # def get_total_cost(self):
    #     return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    brand = models.CharField(max_length=50, blank=True)
    product = models.CharField(max_length=50, blank=True)
    #order=models.ForeignKey(Order, blank=True, related_name='items', on_delete=models.CASCADE)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=1)
    class Meta:
        ordering = ('order',) #sorting by name
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        def __int__(self):
            return self.id

    def sub_total(self):
            return float(self.price) * self.quantity
