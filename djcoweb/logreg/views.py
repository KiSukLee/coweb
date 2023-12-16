from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . models import User

# Create your views here.
def logreg(request):
    return render(request, "logreg/logreg.html")
def validate(request):
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    return redirect()
def dashboard(request, session):
    return render(request, "logreg/dashboard.html")