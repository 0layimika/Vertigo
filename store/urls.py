from django.contrib import admin
from django.urls import path, include
from . import views

# app_name = "store"
urlpatterns=[
    path('',views.home.as_view(), name="home"),
    path('shirts/',views.shirts_view,name="shirts"),
    path('sweats/',views.sweats_view,name='sweats'),
    path('shorts/',views.shorts_view,name='shorts'),
    path('accessories/',views.accessories_view,name='accessories'),
    path('details/<int:product_id>',views.product_detail,name="details"),
    path('cart/<int:product_id>',views.add_to_cart,name="cart"),
    path('cart_item/',views.cart,name="cart_item"),
    path('remove/<int:cart_item_id>',views.cart_remove,name='remove'),
    path('checkout/',views.checkout,name='checkout'),
    path('update/<int:cart_item_id>',views.cart_update,name='update'),
    path('search/',views.search,name='search'),
    path('payment/callback',views.payment_callback, name='payment_callback')

]