from django.urls import path, include
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('artworks', views.artworks, name='artworks'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('gallery', views.gallery, name='gallery'),
    path('museum', views.museum, name='museum'),
    path('shopbar', views.shopbar, name='shopbar'),

]