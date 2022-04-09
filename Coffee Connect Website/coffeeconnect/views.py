from django.shortcuts import render
from .models import Order 
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def home(request):
    return render(request, 'coffeeconnect/homepage.html')

@login_required
def coffee(request):
    context = {
        'order': Order.objects.all()
    }
    return render(request, 'coffeeconnect/coffeepage.html', context)

def logout(request):
    return render(request, 'coffeeconnect/LogoutPage.html')

def login(request):
    return render(request, 'users/loginpage.html')

def register(request):
    return render(request, 'users/registerpage.html')