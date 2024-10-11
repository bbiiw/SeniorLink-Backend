from django.db import models
from company.models import Company

class JobCategory(models.Model):
    category_name = models.CharField(max_length=100)

class Skill(models.Model):
    name = models.CharField(max_length=100)

class JobPosition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

