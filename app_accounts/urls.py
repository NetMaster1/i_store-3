from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('password_change', views.password_change, name='password_change'), 
    # path('person_profile', views.person_profile, name='person_profile'), 
    path('entity_profile', views.entity_profile, name='entity_profile'), 
]