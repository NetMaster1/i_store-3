from django.urls import path
from . import views

urlpatterns = [
    path('', views.email, name='email'),
    path('send_file', views.send_file, name='send_file')
    
]
