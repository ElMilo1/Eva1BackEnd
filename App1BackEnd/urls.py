from django.contrib import admin
from django.urls import path , include
from App1BackEnd import views as App1

urlpatterns = [
    path('',App1.Home),
    path('product1/',App1.Product1),
    path('product2/',App1.Product2),
    path('product3/',App1.Product3)
]
