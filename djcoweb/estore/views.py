from django.http import request
from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Product, Cart, User, Inventory
# Create your views here.

def about(request):
    return render(request, "estore/info.html")

def products(request):
    return render(request, "estore/inventory.html", {"products":Inventory.objects.all()})

def modify_cart(request, action, productid):
    inventory = Inventory.objects.get(id = productid)
    #Should change name to email for user access
    this_user = User.objects.get(name = request.session["name"])
    this_cart = Cart.objects.get_or_create(total = 0, user = this_user)
    this_product = Product.objects.get_or_create(product_id = productid, quantity = 0)
    
    request.session["cart"] = this_cart[0].id
    print(this_cart)    
    print(this_product)
    
    #Add to Cart
    if action == "add":
        if not inventory.quantity > 0:
            messages.error(request, "Out of stock")
            return redirect("/estore/products")
        inventory.quantity -= 1
        inventory.save()
        if this_cart[0].products:
            this_product[0].quantity += 1
        else:
            this_product[0].quantity = 1
        this_product[0].save()
        this_cart[0].products.add(this_product[0])
        return redirect("/estore/products")
    
    #Remove from Cart
    else:
        if not this_cart[0].products.get(this_product[0]):
            messages.error(request, "Insufficient amount")
            return redirect("/estore/products")
        this_product[0].quantity -= 1
        this_product[0].save()
        if this_product[0].quantity < 1:
            print(this_product[0].quantity)
            this_product[0].delete()
            return redirect("/estore/products")
        else:
            inventory.quantity += 1
            inventory.save()
            print(inventory.quantity)
            return redirect("/estore/products")

def cart(request):
    return render(request, "estore/cart.html")