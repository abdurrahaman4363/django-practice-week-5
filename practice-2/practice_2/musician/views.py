from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account has been created successfully")
            return redirect("register")

    else:
        register_form = forms.RegisterForm()
    return render(request, "register.html", {"form": register_form, "type": "Register"})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            userpass = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=userpass)
            if user is not None:
                messages.success(request, "Logged in successfully")
                login(request, user)
                return redirect("musician_list")

    else:
        form = AuthenticationForm()

    return render(request, "register.html", {"form": form, "type": "Login"})


@login_required
def edit_musician(request):
    if request.method == "POST":
        musician_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if musician_form.is_valid():
            musician_form.save()
            messages.success(request, "Edited successfully")
            return redirect("musician_list")

    else:
        musician_form = forms.ChangeUserForm(instance=request.user)
    return render(request, "update_musician.html", {"form": musician_form})


def user_logout(request):
    logout(request)
    return redirect("user_login")
