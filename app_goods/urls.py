from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing', views.listing, name='listing'),
    path('listing_smartphone', views.listing_smartphone, name='listing_smartphone'),
    path('listing_smartwatch', views.listing_smartwatch, name='listing_smartwatch'),
    path('listing_sim', views.listing_sim, name='listing_sim'),
    path('listing_lte', views.listing_lte, name='listing_lte'),
    path('listing_accessory', views.listing_accessory, name='listing_accessory'),
  
    #path('<slug:category_slug>', views.category, name='products_by_category'),
    path('<int:product_id>', views.productPage, name='product_detail'),
    path('accessory/<int:accs_id>', views.accessoryPage, name='accessory_detail'),
    
    path('cart/add/<slug:product_slug>', views.add_cart, name='add_cart'),#строка для вывода товара по slug из карточки товара в корзину 
    # path('cart/add/<slug:accessory_slug>', views.add_cart_accs, name='add_cart_accs'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('search', views.search, name='search'),

]
