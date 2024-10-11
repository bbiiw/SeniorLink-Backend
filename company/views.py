from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, CompanyCategory
from .serializers import CompanySerializer, CompanyCategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from company.permissions import CompanyPermission

class CompanyProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, company_id=None):
        # กรณีที่มี company_id (ดูโปรไฟล์ของผู้สมัครคนอื่น)
        if company_id is not None:
            company = Company.objects.get(id=company_id)
            serializer = CompanySerializer(company)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # กรณีไม่มี company_id (ดูโปรไฟล์ของผู้ที่ล็อกอิน)
        company = Company.objects.get(user=request.user)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # สร้างโปรไฟล์สำหรับบริษัทใหม่
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # อัปเดตโปรไฟล์ของบริษัท
        company = Company.objects.get(user=request.user)
        self.check_object_permissions(request, company)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyCategoryView(APIView):
    def get(self, request):
        category = CompanyCategory.objects.all()
        serializer = CompanyCategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanyCategorySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
