from django.http import request
from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Product, Cart, User, Inventory
# Create your views here.

def about(request):
    return render(request, "estore/info.html")

def products(request):
    return render(request, "estore/inventory.html", {"products":Inventory.objects.all()})

def modify_cart(request, action, product_id):
    inventory = Inventory.objects.get(id = product_id)
    #Should change name to email for user access
    this_user = User.objects.get(name = request.session["name"])
    this_cart = Cart.objects.filter(user = this_user).last()
    
    if not this_cart:
        Cart.objects.create(total = 0, user = this_user, products = Product.objects.create(product_id = product_id, quantity = 0))
    
    this_product = Product.objects.filter(product_id = product_id).last()
    
    #Add to Cart
    if action == "add":
        if not inventory.quantity > 0:
            messages.error(request, "Out of stock")
            return redirect(request, "products")
        inventory.quantity -= 1
        inventory.save()
        if this_cart.products:
            this_product.quantity += 1
        else:
            this_product.quantity = 1
        this_product.save()
        this_cart.products.add(this_product)
        return redirect(request, "products")
    
    #Remove from Cart
    else:
        if not this_cart.products.get(this_product):
            messages.error(request, "Insufficient amount")
            return redirect(request, "products")
        this_product.quantity -= 1
        this_product.save()
        if this_product.quantity < 1:
            this_cart.objects.delete(products = this_product)
            return redirect(request, "products")
        else:
            inventory.quantity += 1
            inventory.save()
            return redirect(request, "products")

def cart(request):
    return render(request, "estore/cart.html")