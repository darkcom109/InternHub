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

class Internship(models.Model):
    website = models.CharField(max_length=255)
    related_roles = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

internshipOne = Internship(1, 'Bristol Tracker - Tech', 'Software Engineer, IT', 'https://app.the-trackr.com/uk-technology/summer-internships')
internshipOne.save()
internshipTwo = Internship(2, 'Bristol Tracker - Finance', 'Finance, Banking', 'https://app.the-trackr.com/uk-finance/summer-internships')
internshipTwo.save()
internshipThree = Internship(3, 'Bristol Tracker - Law', 'Law', 'https://app.the-trackr.com/uk-law/summer-internships')
internshipThree.save()
internshipFour = Internship(4, 'Bristol Tracker - North America Application', 'NA Finance', 'https://app.the-trackr.com/na-finance-2027/summer-internships')
internshipFour.save()
