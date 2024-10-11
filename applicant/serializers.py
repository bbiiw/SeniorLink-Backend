from rest_framework import serializers
from .models import Applicant, Education
from job.models import Skill

class EducationSerializer(serializers.ModelSerializer):
    end_year = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = Education
        fields = ['name', 'faculty', 'major', 'start_year', 'end_year']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class ApplicantSerializer(serializers.ModelSerializer):
    education = EducationSerializer()
    skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    myskills = SkillSerializer(source='skills', many=True, read_only=True)

    birth_date = serializers.DateField(format="%d/%m/%Y")

    class Meta:
        model = Applicant
        fields = [
            'id', 'first_name', 'last_name', 'gender', 'birth_date', 'email', 
            'phone_number', 'address', 'description', 'profile_picture', 'skills', 'myskills', 'education'
        ]

    def create(self, validated_data):
        # ดึงข้อมูลออกมา
        education_data = validated_data.pop('education')
        skills_data = validated_data.pop('skills')

        applicant = Applicant.objects.create(**validated_data)
        Education.objects.create(applicant=applicant, **education_data)
        applicant.skills.set(skills_data)
        
        return applicant

    def update(self, instance, validated_data):
        # ดึงข้อมูลออกมา
        education_data = validated_data.pop('education', None)
        skills_data = validated_data.pop('skills', None)
        
        # อัปเดต Applicant
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # อัปเดต Education
        if education_data:
            education = instance.education
            for attr, value in education_data.items():
                setattr(education, attr, value)
            education.save()
        
        # อัปเดต Skills
        if skills_data is not None:
            instance.skills.set(skills_data)
        
        return instance
