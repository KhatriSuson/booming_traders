from django.contrib import admin
from django.urls import path
from bloom_app import views

# from bloom_app.views import  DetailView, ContactView, CheckoutView, CartView
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.IndexView.as_view()),
    path("shop/", views.ShopView.as_view(), name="shop"),
    path("detail/", views.DetailView.as_view(), name="detail"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("cart/", views.CartView.as_view(), name="cart"),
]
