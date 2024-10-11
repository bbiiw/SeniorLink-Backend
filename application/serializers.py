from rest_framework import serializers
from .models import Application, Status
from applicant.serializers import ApplicantSerializer
from job.serializers import JobPositionSerializer

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)
    job = JobPositionSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'applicant', 'job', 'status', 'application_date']
