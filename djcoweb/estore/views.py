from django.http import request, JsonResponse
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

def modify_cart(request, method, action, product_id):
    inventory = Inventory.objects.get(id = product_id)
    this_user = User.objects.get(email = User.objects.get(name = request.session['name']).email)
    this_cart = Cart.objects.get(id = request.session["cart_id"], user = this_user)
    data = {}
    
    #based on which template sent the fetch request, values and methods used change accordingly
    if method == 'product':
        formData = 1
        this_product = this_cart.products.filter(product_id = product_id)
    else:
        this_product = this_cart.products.get(product_id = product_id)
        formData = request.POST['quantity']

    if formData == "Quantity":
        return JsonResponse(data)
    
    #Add to Cart
    if action == "add":
        if not inventory.quantity > 0 or int(formData) > inventory.quantity:
            #messages.error(request, "Out of stock")
            data['error'] = "Out of stock"
            return JsonResponse(data)
        print(formData)
        inventory.quantity -= int(formData)
        inventory.save()
        if not this_product:
            this_product = Product.objects.create(product_id = product_id, quantity = 1)
            this_cart.products.add(this_product)
        else:
            this_product = this_cart.products.get(product_id = product_id)
            this_product.quantity += int(formData)
            this_product.save()
            #this_cart.products.add(this_product)
        this_cart.total += inventory.price * int(formData)
        this_cart.save()
        print(this_cart.total)
        print(this_product.product_id)
        print(this_product.quantity)
        #return prod_cart(method)
    
    #Remove from Cart
    else:
        if not this_product or this_product.quantity < int(formData):
            data['error'] = "Insufficient amount in cart"
            return JsonResponse(data)
        this_product.quantity -= int(formData)
        this_product.save()
        print(this_product.product_id)
        print(this_product.quantity)
        if this_product.quantity < 1:
            print(this_product.quantity)
            this_product.delete()
        this_cart.total -= inventory.price * int(formData)
        this_cart.save()
        print(this_cart.total)
        inventory.quantity += int(formData)
        inventory.save()
    
    #Send data to fetch request
    data = {"name":inventory.name, "price":inventory.price}
    if method == 'product':
        data["quantity"] = inventory.quantity
    else:
        data["quantity"] = this_product.quantity
        data["total"] = this_cart.total
    return JsonResponse(data)

def cart(request, method):
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
    if method == "checkout":
        return render(request, "estore/checkout.html", context = {"prods":prods, "total":cart.total})
    return render(request, "estore/cart.html", context = {"prods":prods, "total":cart.total})


    
#curl -v -X POST "https://api-m.sandbox.paypal.com/v1/oauth2/token"\
# -u "AcBafemIl_XatSuGWN8GlpMDuiGYJ3rUL2oeZkAxezPdIfk9LZcdwU41Ye1Ght08KOsQjnVakDt66PRn:EB5uN9Gwi-YhQmomkaDaJFao5DfEOvBiXQF5NICptk512y9dJkNOfi4TjTB4pjjrVDGOXl9FIALzU_EG"\
# -H "Content-Type: application/x-www-form-urlencoded"\
# -d "grant_type=client_credentials"
      