from django import forms

# Imports the Django's built-in User model
# This stores usernames, passwords, emails
from django.contrib.auth.models import User

# The Meta class is Django's secret handshake between your form and the model
# It tells Django which model to base the form on, and which fields to include

class SignupForm(forms.ModelForm):
    class Meta:
        model = User # Which model to base it on
        fields = ['username', 'email', 'password'] # Whichever fields you want

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password'] # Whichever fields you want