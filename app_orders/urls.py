from django.urls import path
from . import views

urlpatterns = [
    path('order_create', views.order_create, name='order_create'),
    path('edit_order/<int:order_id>', views.edit_order, name='edit_order'),
    path('edit_customer_name/<int:order_id>', views.edit_customer_name, name='edit_customer_name'),
    path('anonymous_pick_up', views.anonymous_pick_up, name='anonymous_pick_up'),
    # path('', views.delivery, name='delivery'),
    path('delivery_choice/<int:order_id>', views.delivery_choice, name='delivery_choice'),
    path('customer_choice/<int:order_id>', views.customer_choice, name='customer_choice'),
    path('logistics_choice/<int:order_id>', views.logistics_choice, name='logistics_choice'),
    path('payment_choice/<int:order_id>', views.payment_choice, name='payment_choice'),
    
    # path('payment_stripe', views.payment_stripe, name='payment_stripe'),
    path('orders_history', views.orders_history, name='orders_history'),
    path('GeneratePDF/<pk>', views.GeneratePDF.as_view(), name="GeneratePDF"),
    path('DownloadPDF/<pk>', views.DownloadPDF.as_view(), name="DownloadPDF"),

    path('email', views.email, name='email'),
    path('send_file', views.send_file, name='send_file'),
    path('send_stored_file/<pk>', views.send_file, name='send_stpred_file')
  

]
