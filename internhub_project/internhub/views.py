from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, JobForm
from .models import Job, Internship
from django.contrib.auth.models import User

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
    # Query only the current user
    user_jobs = Job.objects.filter(user=request.user).order_by('-created_at')
    # Optionally add some quick stats
    stats = {
        'total': user_jobs.count(),
        'applied': user_jobs.filter(status='applied').count(),
        'interview': user_jobs.filter(status='interview').count(),
        'offer': user_jobs.filter(status='offer').count(),
    }

    context = {
        'jobs': user_jobs,
        'stats': stats,
    }
    return render(request, 'dashboard.html', context)

# The add_job view is responsible for adding a job to the dashboard
# If the form is posted, it fills out the JobForm instance with the data
# If the data is valid, it saves it to the database (adds current user to the job beforehand)
# If the request is GET, it shows an empty form
@login_required
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

# The edit_job view is responsible for editing a specific job according to the job_id
# It finds the job object using the job_id and according to the current user for security purpose
# instance=job essentially fills out the form with the job data so the user can view the data they already wrote
@login_required
def edit_job(request, job_id):
    # Find the job owned by the logged-in user
    job = get_object_or_404(Job, id=job_id, user=request.user)
    form = JobForm(instance=job)
    print(job.company)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect after successful update
    
    else:
        # Only create a new instance form for GET requests
        form = JobForm(instance=job)

    return render(request, 'edit_job.html', {'form': form, 'job': job})

# The delete_job is responsible for deleting posts
# If a user deletes a post, the job_id is passed into the view
# This post is then found in the database and deleted using .delete()
@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, user=request.user)

    if request.method == "POST":
        job.delete()
    
    return redirect('dashboard')

@login_required
def internships(request):
    internships = Internship.objects.all()
    return render(request, 'internships.html', {'internships': internships})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)