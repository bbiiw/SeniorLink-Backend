from django.db import models
from applicant.models import Applicant
from job.models import JobPosition

class Status(models.Model):
    name = models.CharField(max_length=100)

class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
