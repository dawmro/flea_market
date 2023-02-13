from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        # model to use: default User model that comes from django
        model = User
        # fields for user to fill out
        fields = ('username', 'email', 'password1', 'password2')
    
    # modify looks of user field
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username goes here',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    # modify looks of email field
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Email goes here',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    # modify looks of password1 field
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Password goes here',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    # modify looks of password2 field
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Repeat Your Password here',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))