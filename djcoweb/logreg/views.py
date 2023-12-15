from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import User

# Create your views here.
def logreg(request):
    return render(request, "logreg/logreg.html")
def create(request):
    if validate(request.post):
        return redirect('dashboard')
    return redirect('/')
def match(request):
    if validate(request.post):
        return redirect('dashboard')
    return redirect('/')
def validate(request, context):
    if context[submit] == 'create':
        value = False
        if context['name'] <= 3:
            flash('Name must be at least 3 characters long')
        if context['email']:
            flash('Invalid email')
        if len(context['number']) != 10:
            flash('Invalid phone number')
        if context['pword'] < 8:
            flash('Password must be at least 8 characters')
        else:
            value = True
        return value
    else:
        value = False
        if User.objects.get['email'] != context['name']:
            flash("User does not exist")
        if User.objects.get['pword'] != context['pword']:
            flash("Incorrect password")
        else:
            value = True
        return value
def dashboard(request, session):
    return render(request, "logreg/dashboard.html")