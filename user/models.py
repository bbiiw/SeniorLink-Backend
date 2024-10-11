from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('applicant', 'Applicant'),
        ('company', 'Company')
    ]

    role = models.CharField(choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)