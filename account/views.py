from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('products:product_list')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('products:product_list')
                else:
                    return HttpResponse("Disabled Account")
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    context = {
        'form'  :   form,
    }
    return render(request, 'account/login.html', context)

def user_logout(request):
    logout(request)
    return render(request, "account/logout.html", {})

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('products:product_list')
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, "account/signup_done.html", {'new_user' : new_user})
    else:
        form = RegistrationForm()
    context = {
        'form'  :   form,
    }
    return render(request, "account/register.html", context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = EditProfileForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, "account/edit_profile.html", context)
