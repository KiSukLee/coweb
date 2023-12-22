from django.urls import path
from . import views

app_name = "estore"

urlpatterns = [
    path("about", views.about),
    path("products", views.products),
    path("<str:action>/<int:productid>", views.modify_cart),
    path("cart", views.cart)
]