import bcrypt
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . models import User
from estore.models import Cart

# Create your views here.
def logreg(request):
    return render(request, "logreg/logreg.html")
def validate(request):
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        #return JsonResponse(errors)
        return redirect('/logreg/logreg')
    if request.POST['form'] == 'create':
        user = User.objects.create(name=request.POST['name'], email=request.POST['email'], number=request.POST['number'], password=bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt()).decode())
        Cart.objects.create(user = user, total = 0)
    request.session['name'] = User.objects.get(email = request.POST['lemail']).name
    request.session['cart_id'] = Cart.objects.filter(user = User.objects.get(name = request.session["name"])).last().id
    return redirect('/logreg/dashboard')
def dashboard(request):
    return render(request, "logreg/dashboard.html")
def logout(request):
    del request.session['name']
    return redirect('/logreg/logreg')