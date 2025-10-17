from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your models here.

class Job(models.Model):
    # Restrict status to these choices
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('offer', 'Offer Received'),
        ('rejected', 'Rejected'),
        ('saved', 'Saved / Draft'),
        ('ghosted', 'Ghosted/Ignored'),
        ('assessment', 'Assessment Required'),
    ]
    
    # Links to an actual user from the database
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    deadline = models.DateField(null=True, blank=True)
    link_to_application = models.CharField(max_length=255, default="None")
    created_at = models.DateTimeField(auto_now_add=True)

class Internship(models.Model):
    website = models.CharField(max_length=255)
    related_roles = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
