from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from .forms import ChangeUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from car.models import Car
from . import models

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


class UserLoginView(LoginView):
    template_name = "register.html"

    def get_success_url(self):
        return reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "loged in succcessfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "loged in information incorrect")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


# @login_required
# def profile(request):
#     car = Car.objects.filter()
#     return render(request, "profile.html", {"car": car})


@login_required
def purchase_car(request, id):
    car = Car.objects.get(pk=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        purchased_cars = [car]
        return render(request, "profile.html", {"purchased_cars": purchased_cars})
    else:
        return render(request, "home.html")


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile Updated successfully")
            return redirect("profile")

    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, "update_profile.html", {"form": profile_form})


def user_logout(request):
    logout(request)
    return redirect("user_login")


# class UserLogoutView(LogoutView):
#     template_name = "register.html"

#     def get_success_url(self):
#         return reverse_lazy("home")


class DetailPCarView(DetailView):
    model = models.Car
    pk_url_kwarg = "id"
    template_name = "car_details.html"

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
