from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    # Checks if the request.method contains "POST", this means that the form was submitted
    if request.method == "POST":
        form = SignupForm(request.POST) # Make a form object and place in the data

        # Checks if the data is valid (all fields required + valid)
        if form.is_valid():
            # If the data passes validation, it saves the new user to the database
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})