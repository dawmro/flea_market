from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        # model to use: default User model that comes from django
        model = User
        # fields for user to fill out
        fields = ('username', 'email', 'password1', 'password2')