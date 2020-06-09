from django.contrib import admin
from .models import Product, Cart, CartItem, Brand, Category, Accessory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name')
    prepopulated_fields = {'slug': ('model_name','colour','ram' )}

class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    prepopulated_fields = {'slug': ('name','link')}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart_id', 'date_added')#dispays columns we need
    list_per_page = 25

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')
    list_per_page = 25
    list_filter = ('cart', 'product' )#creates a filter at the side panel

# Register your models here.
admin.site.register(Product, ProductAdmin),
admin.site.register(Accessory, AccessoryAdmin),
admin.site.register(Cart, CartAdmin),
admin.site.register(CartItem, CartItemAdmin),
admin.site.register(Brand, BrandAdmin),
admin.site.register(Category, CategoryAdmin),

