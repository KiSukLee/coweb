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
    this_cart = Cart.objects.get(user = this_user, id = request.session["cart_id"])
    
    print(this_user.name)
    print(this_cart.id)
    #Add to Cart
    if action == "add":
        if not inventory.quantity > 0:
            messages.error(request, "Out of stock")
            return redirect("/estore/products")
        inventory.quantity -= 1
        inventory.save()
        if this_cart.products.filter(product_id = product_id):
            this_product = Product.objects.get(product_id = product_id)
            this_product.quantity += 1
            this_product.save()
            this_cart.products.add(this_product)
        else:
            this_product = Product.objects.create(product_id = product_id, quantity = 1)
            this_cart.products.add(this_product)
        print(this_cart.products.get(product_id = product_id).product_id)
        print(this_cart.products.get(product_id = product_id).quantity)
        return redirect("/estore/products")
    
    #Remove from Cart
    else:
        if this_cart.products.filter(product_id = product_id) == None:
            messages.error(request, "Insufficient amount")
            return redirect("/estore/products")
        this_product = Product.objects.get(product_id = product_id)
        this_product.quantity -= 1
        this_product.save()
        print(this_cart.products.get(product_id = product_id).product_id)
        print(this_cart.products.get(product_id = product_id).quantity)
        if this_product.quantity < 1:
            this_cart.products.get(product_id = product_id).delete()
            return redirect("/estore/products")
        else:
            inventory.quantity += 1
            inventory.save()
            return redirect("/estore/products")

def cart(request):
    return render(request, "estore/cart.html")