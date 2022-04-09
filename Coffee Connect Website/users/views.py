from django.shortcuts import render, redirect
from django.contrib import messages
from .regforms import UserRegisterForm
from django.utils.translation import gettext_lazy as _


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
       
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/registerpage.html',{'form':form})
