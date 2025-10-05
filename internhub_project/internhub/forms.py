from django import forms
from django.contrib.auth.forms import UserCreationForm

# Imports the Django's built-in User model
# This stores usernames, passwords, emails
from django.contrib.auth.models import User
from .models import Job

# The Meta class is Django's secret handshake between your form and the model
# It tells Django which model to base the form on, and which fields to include

class SignupForm(UserCreationForm):

    email = forms.EmailField(required=True) # Needs to be included manually

    class Meta:
        model = User # Which model to base it on
        fields = ['username', 'email', 'password1', 'password2'] # Whichever fields you want

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'position', 'status', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }