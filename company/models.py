from django.db import models
from user.models import User

class CompanyCategory(models.Model):
    category_name = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    logo = models.ImageField(upload_to='company_logo/', blank=True, null=True)
    background_image = models.ImageField(upload_to='company_background/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)
