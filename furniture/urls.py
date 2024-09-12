from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.viewhome,name='home'),
    path('shop/',views.viewshop,name='shop'),
    path('about/',views.viewabout,name='about'),
    path('services/',views.viewservices,name='services'),
    path('contact/',views.viewcontact,name='contact'),
    path('login/',views.viewloginregister,name='login'),
    path('logout/',views.viewlogout,name='logout'),
    path('register/',views.viewregister,name='register')
]