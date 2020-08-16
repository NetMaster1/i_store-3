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
    path('cart/remove/<slug:product_slug>', views.remove_from_cart, name='remove_from_cart'),
    path('cart/remove/<slug:product_slug>', views.delete_cartitem, name='delete_cartitem'),

    # path('cart/add/<slug:accessory_slug>', views.add_cart_accs, name='add_cart_accs'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('gen_search', views.gen_search, name='gen_search'),
    path('search_smartphone', views.search_smartphone, name='search_smartphone'),
    path('search_smartwatch', views.search_smartwatch, name='search_smartwatch'),
    path('search_accessory', views.search_accessory, name='search_accessory'),
    path('search_sim', views.search_sim, name='search_sim'),
    path('search_lte', views.search_lte, name='search_lte'),
    


]
