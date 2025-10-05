from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    # Checks if the request.method contains "POST", this means that the form was submitted
    if request.method == "POST":
        form = SignupForm(request.POST) # Make a form object and place in the data

        # Checks if the data is valid (all fields required + valid)
        if form.is_valid():
            # If the data passes validation, it saves the new user to the database
            form.save()
            messages.success(request, "Signup was Successful!")
            return redirect('login')
        else:
            messages.error(request, "Signup was Unsuccessful!")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})

def login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.data['username']
            password = form.data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "You have logged in successfully!")
                return redirect('dashboard') # Success!
            else:
                messages.error(request, "Incorrect Username or Password")
                return render(request, "login.html", {"form": form, "error": "Invalid username or password"})
        else:
            return render(request, "login.html", {"form": form, "error": "Invalid username or password"})
    
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')