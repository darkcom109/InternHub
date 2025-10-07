from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    # Restrict status to these choices
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('offer', 'Offer Received'),
        ('rejected', 'Rejected'),
        ('saved', 'Saved / Draft'),
    ]
    
    # Links to an actual user from the database
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
