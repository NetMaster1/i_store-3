from django.contrib import admin
from .models import Product, Cart, CartItem, Brand, Category, Accessory, Color, Operator, Tarif, Com_type, Sensor, Body_material, Lace_material, Biometrics, Security_class

class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'category', 'image')
    prepopulated_fields = {'slug': ('brand','model_name', 'color', 'hdd','ram' )}
    list_filter = ('category','brand',)#creates a filter at the side panel

class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    prepopulated_fields = {'slug': ('name','link')}
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class OperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class TarifAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class Com_typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class Body_materialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class Lace_materialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class BiometricsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class Security_classAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
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
admin.site.register(Color, ColorAdmin),
admin.site.register(Operator, OperatorAdmin),
admin.site.register(Tarif, TarifAdmin),
admin.site.register(Com_type, Com_typeAdmin),
admin.site.register(Sensor, SensorAdmin),
admin.site.register(Body_material, Body_materialAdmin),
admin.site.register(Lace_material, Lace_materialAdmin),
admin.site.register(Biometrics, BiometricsAdmin),
admin.site.register(Security_class, Security_classAdmin),




