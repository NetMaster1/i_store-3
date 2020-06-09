from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product','price', 'quantity')

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email','phone', 'postal_code', 'region', 'city')#displays columns we need
    #list_display_links = ('id', 'brand', 'model_name')#makes linkabable columns we need
    #list_filter = ('brand', )#creates a filter at the side panel
    #list_editable = ('in_stock',) #lets edit boolean vaules
    #search_fields = ('model_name', 'battery')#creates a search field
    list_per_page = 25
    inlines=[OrderItemInline]

# Register your models here.
admin.site.register(OrderItem, OrderItemAdmin),
admin.site.register(Order, OrderAdmin)
