from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Applicant
from .serializers import ApplicantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from applicant.permissions import ApplicantPermission

class ApplicantProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, applicant_id=None):
        # กรณีที่มี applicant_id (ดูโปรไฟล์ของผู้สมัครคนอื่น)
        if applicant_id is not None:
            applicant = Applicant.objects.get(id=applicant_id)
            serializer = ApplicantSerializer(applicant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # กรณีไม่มี applicant_id (ดูโปรไฟล์ของผู้ที่ล็อกอิน)
        applicant = Applicant.objects.get(user=request.user)
        serializer = ApplicantSerializer(applicant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # สร้างโปรไฟล์สำหรับผู้สมัครงานใหม่
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # อัปเดตโปรไฟล์ของผู้สมัครงาน
        applicant = Applicant.objects.get(user=request.user)
        self.check_object_permissions(request, applicant)
        serializer = ApplicantSerializer(applicant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
