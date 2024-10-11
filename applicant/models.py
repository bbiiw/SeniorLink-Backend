from django.db import models
from user.models import User
from job.models import Skill

class Applicant(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES)
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True)

class Education(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    start_year = models.IntegerField(default=0, blank=True)
    end_year = models.IntegerField(default=0, blank=True)
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE)
