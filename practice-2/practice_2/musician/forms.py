from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"id": "required"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    instrument_type = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "instrument_type",
        ]


class ChangeUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
