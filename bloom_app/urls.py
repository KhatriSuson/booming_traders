from django.contrib import admin
from django.urls import path
from bloom_app import views
from bloom_app.views import IndexView, ShopView
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view()),
    path("shop/", ShopView.as_view(), name="shop"),
    
    
    
    
]
