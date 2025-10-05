from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

# Create your views here.
# Every view requires a request object for processing
# Django chooses to be explicit with their request object parameter in each view

# The index view is responsible for rendering the index.html page
# This a simple welcome page outlining the features of InternHub and enables
# users to be able to create an account or login to their current account
def index(request):
    return render(request, 'index.html')

# The signup view is responsible for creating a user account into the database
# 1) The first condition checks if the user is authenticated, if so, it redirects them directly to their dashboard
# 2) Verifies if the request object contains a 'POST' method, which then uses the data to make a form object
# 3) Then it checks if the data is valid, then saves it to the database using form.save()
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

# The login view is responsible for logging in the user to their account
# 1) We first check if the user is authenticated already
# 2) Then we check if the method in the request object is 'POST', meaning the form was submitted
# 3) If so, we extract the 'username' and 'password' and authenticate it with the database
# 4) If it is authenticated, we redirect the user into their account and log them in using auth_login()
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

# The logout view is responsible for ensuring that the user is logged out of their current session
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect('login')

# The dashboard is responsible for displaying all the data once the user is logged in
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')