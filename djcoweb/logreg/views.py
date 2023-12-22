import bcrypt
from django.http import HttpResponse, request
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
        return redirect('/')
    if request.POST['form'] == 'create':
        User.objects.create(name=request.POST['name'], email=request.POST['email'], number=request.POST['number'], password=bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt()).decode())
        request.session['name'] = request.POST['name']
    else:
        request.session['name'] = User.objects.get(email = request.POST['email']).name
    return redirect('/dashboard')
def dashboard(request):
    return render(request, "logreg/dashboard.html")
def logout(request):
    del request.session['name']
    return redirect('/')