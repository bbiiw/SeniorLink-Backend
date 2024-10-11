from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class ApplicantRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        applicant = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role='applicant'
        )
        applicant.set_password(validated_data['password'])
        applicant.save()
        return applicant

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"message": "รหัสผ่านไม่ตรงกัน!"})
        return data

class CompanyRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        company = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role='company'
        )
        company.set_password(validated_data['password'])
        company.save()
        return company

    # ตรวจสอบว่า password ตรงกันหรือไม่
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"message": "รหัสผ่านไม่ตรงกัน!"})
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # ตรวจสอบว่ามีผู้ใช้ที่มีอีเมลนี้ในระบบหรือไม่
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'message': 'ไม่พบผู้ใช้งานที่มีอีเมลนี้'})
            
        user = authenticate(username=user.username, password=password)
        if user is None:
            raise serializers.ValidationError({"message": "รหัสผ่านไม่ถูกต้อง"})
        
        data['user'] = user
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
