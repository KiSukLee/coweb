from django.http import request
from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Product, Cart, User, Inventory
# Create your views here.

def about(request):
    try:
        name = request.session['name']
    except:
        name = False
    return render(request, "estore/info.html", {"name": name})

def products(request):
    try:
        name = request.session['name']
    except:
        name = False
    return render(request, "estore/inventory.html", {"products":Inventory.objects.all(), "name": name})

def prod_cart(method):
    if method == "products":
        return redirect("/products")
    return redirect("/cart")

def modify_cart(request, method, action, product_id):
    inventory = Inventory.objects.get(id = product_id)
    this_user = User.objects.get(email = User.objects.get(name = request.session['name']).email)
    this_cart = Cart.objects.get(id = request.session["cart_id"], user = this_user)
    
    print(this_cart.user.name)
    print(this_cart.id)
    #Add to Cart
    if action == "add":
        if not inventory.quantity > 0:
            messages.error(request, "Out of stock")
            return prod_cart(method)
        inventory.quantity -= 1
        inventory.save()
        if this_cart.products.filter(product_id = product_id):
            this_product = this_cart.products.get(product_id = product_id)
            this_product.quantity += 1
            this_product.save()
            this_cart.products.add(this_product)
        else:
            this_product = Product.objects.create(product_id = product_id, quantity = 1)
            this_cart.products.add(this_product)
        this_cart.total += inventory.price
        this_cart.save()
        print(this_cart.total)
        print(this_cart.products.get(product_id = product_id).product_id)
        print(this_cart.products.get(product_id = product_id).quantity)
        return prod_cart(method)
    
    #Remove from Cart
    else:
        if not this_cart.products.filter(product_id = product_id):
            messages.error(request, "Insufficient amount")
            return prod_cart(method)
        this_product = this_cart.products.get(product_id = product_id)
        this_product.quantity -= 1
        this_product.save()
        print(this_product.product_id)
        print(this_product.quantity)
        if this_product.quantity < 1:
            print(this_product.quantity)
            this_cart.products.get(product_id = product_id).delete()
        this_cart.total -= inventory.price
        this_cart.save()
        print(this_cart.total)
        inventory.quantity += 1
        inventory.save()
        return prod_cart(method)

def cart(request):
    cart = Cart.objects.get(id = request.session['cart_id'])
    products = cart.products.all()
    prods = []
    for product in products:
        prod = {
            "prod_id":product.product_id,
            "name":Inventory.objects.get(id = product.product_id).name,
            "price":Inventory.objects.get(id = product.product_id).price,
            "quantity":product.quantity
        }
        prods.append(prod)
    print(prods)
    return render(request, "estore/cart.html", context = {"prods":prods, "total":cart.total})

def checkout(request):
    return 
    