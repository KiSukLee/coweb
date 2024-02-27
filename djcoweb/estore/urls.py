from django.urls import path
from . import views

app_name = "estore"

urlpatterns = [
    path("", views.about),
    path("products", views.products),
    path("<str:method>/<str:action>/<int:product_id>", views.modify_cart),
    path("cart/<str:method>", views.cart),
]