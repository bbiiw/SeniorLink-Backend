from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Permission, Group
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .serializers import ApplicantRegisterSerializer, CompanyRegisterSerializer, LoginSerializer, UserSerializer

class ApplicantRegisterView(APIView):
    def post(self, request):
        serializer = ApplicantRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ลงทะเบียนผู้สมัครงานสำเร็จ'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyRegisterView(APIView):
    def post(self, request):
        serializer = CompanyRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ลงทะเบียนบริษัทสำเร็จ'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, role):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            if user is not None:
                if user.role == role:
                    login(request, user)
                    
                    # มอบสิทธิ์ให้กับผู้ใช้ตาม role
                    if role == 'applicant':
                        applicant_group, created = Group.objects.get_or_create(name='applicant')
                        user.groups.add(applicant_group)
                    elif role == 'company':
                        company_group, created = Group.objects.get_or_create(name='company')
                        user.groups.add(company_group)

                    token, created = Token.objects.get_or_create(user=user)
                    user_data = UserSerializer(user)
                    return Response({'token': token.key, 'data': user_data.data}, status=status.HTTP_200_OK)
                
            return Response({'message': f'อีเมลนี้เป็นของ {user.role}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "ออกจากระบบสำเร็จ!"}, status=status.HTTP_200_OK)