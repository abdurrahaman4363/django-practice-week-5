from django import forms
from .models import Car, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = "__all__"
        exclude = ["brand"]


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"id": "required"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ChangeUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
