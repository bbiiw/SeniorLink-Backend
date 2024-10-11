from rest_framework import serializers
from company.serializers import CompanySerializer
from .models import Skill, JobCategory, JobPosition

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class JobCategorySerializer(serializers.ModelSerializer):
    job_count = serializers.SerializerMethodField()

    class Meta:
        model = JobCategory
        fields = ['id', 'category_name', 'job_count']

    def get_job_count(self, obj):
        return JobPosition.objects.filter(job_category=obj).count()

class JobPositionSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    job_category = serializers.PrimaryKeyRelatedField(queryset=JobCategory.objects.all())
    skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)

    category = JobCategorySerializer(source='job_category', read_only=True)
    myskills = SkillSerializer(source='skills', many=True, read_only=True)
    
    # กำหนดรูปแบบวันที่เป็น dd/mm/yyyy
    start_date = serializers.DateField(format="%d/%m/%Y")
    end_date = serializers.DateField(format="%d/%m/%Y")
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M")

    class Meta:
        model = JobPosition
        fields = [
            'id', 'title', 'description', 'location', 'duration', 
            'start_date', 'end_date', 'created_at', 'company', 
            'job_category', 'category', 'skills', 'myskills'
        ]
