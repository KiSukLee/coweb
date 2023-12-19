from django.urls import path
from . import views

app_name = "estore"

urlpatterns = [
    path("about", views.about),
    path("products", views.products),
    path("cart", views.cart)
]