from django.shortcuts import render, redirect
from . models import Product
# Create your views here.

def about(request):
    return render(request, "estore/info.html")

def products(request):
    return render(request, "estore/products.html")

def cart(request):
    return render(request, "estore/cart.html")