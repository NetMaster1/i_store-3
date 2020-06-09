from django.urls import path
from . import views

urlpatterns = [
    path('order_create', views.order_create, name='order_create'),
    path('anonymous_pick_up', views.anonymous_pick_up, name='anonymous_pick_up'),
    path('delivery', views.delivery, name='delivery'),
    path('choice', views.choice, name='choice'),
    path('payment_choice', views.payment_choice, name='payment_choice'),
    path('payment_stripe', views.payment_stripe, name='payment_stripe'),
    path('orders_history', views.orders_history, name='orders_history'),
    # path('pdf_page', views.pdf_page, name='pdf_page'),
    # path('pdf_view', views.ViewPDF.as_view(), name="pdf_view"),
    # path('pdf_download', views.DownloadPDF.as_view(), name='pdf_download'),
    path('GeneratePDF/<pk>', views.GeneratePDF.as_view(), name="GeneratePDF"),
    path('DownloadPDF/<pk>', views.DownloadPDF.as_view(), name="DownloadPDF")
  

]