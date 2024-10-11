from rest_framework import serializers
from .models import Company, CompanyCategory

class CompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = ['id', 'category_name']

class CompanySerializer(serializers.ModelSerializer):
    # ใช้ PrimaryKeyRelatedField สำหรับการเขียนข้อมูล
    # ใช้ CompanyCategorySerializer สำหรับการอ่านข้อมูล (nested objects)
    company_category = serializers.PrimaryKeyRelatedField(queryset=CompanyCategory.objects.all(), write_only=True)
    category = CompanyCategorySerializer(source='company_category', read_only=True)

    class Meta:
        model = Company
        fields = [
            'id', 'name', 'description', 'email', 'phone_number', 
            'address', 'logo', 'background_image', 'company_category', 'category'
        ]
