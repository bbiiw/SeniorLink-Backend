from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application, JobPosition, Applicant, Status
from company.models import Company
from .serializers import ApplicationSerializer, StatusSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StatusView(APIView):
    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationListView(APIView):
    def get(self, request):
        company = request.user.company
        applications = Application.objects.filter(job__company=company)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        application = Application.objects.get(pk=id)
        status_id = request.data.get('status')
        application.status_id = status_id
        application.save()
        return Response({"message": "เปลี่ยนแปลงสถานะ"}, status=status.HTTP_200_OK)
        
class ApplicantApplicationView(APIView):
    def get(self, request):
        applicant = Applicant.objects.get(user=request.user)
        applications = Application.objects.filter(applicant=applicant)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, application_id):
        application = Application.objects.get(id=application_id, applicant__user=request.user)
        application.delete()
        return Response({'message': 'ลบใบสมัครงานสำเร็จ'}, status=status.HTTP_204_NO_CONTENT)


class CompanyApplicationView(APIView):
    def get(self, request):
        company = Company.objects.get(user=request.user)
        applications = Application.objects.filter(job__company=company)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, application_id):
        company = Company.objects.get(user=request.user)
        application = Application.objects.get(id=application_id, job__company=company)
        application.delete()
        return Response({'message': 'ลบใบสมัครงานสำเร็จ'}, status=status.HTTP_204_NO_CONTENT)
    
class ApplyForJobView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, job_id):
        job_position = JobPosition.objects.get(id=job_id)
        applicant = Applicant.objects.get(user=request.user)

        if Application.objects.filter(applicant=applicant, job=job_position).exists():
            return Response({'message': 'คุณได้สมัครงานนี้แล้ว'}, status=status.HTTP_400_BAD_REQUEST)

        # สร้างใบสมัครงาน
        pending_status = Status.objects.get(name="รอการพิจารณา")
        application = Application.objects.create(applicant=applicant, job=job_position, status=pending_status)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    
