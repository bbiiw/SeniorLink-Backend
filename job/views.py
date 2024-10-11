from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import JobPosition, JobCategory, Skill, Company
from .serializers import JobPositionSerializer, JobCategorySerializer, SkillSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AllJobPositionListView(APIView):
    """ แสดงงานให้ applicant ดูทั้งหมด """
    def get(self, request):
        job_positions = JobPosition.objects.all().order_by("-created_at")
        serializer = JobPositionSerializer(job_positions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class JobPositionListView(APIView):
    """ แสดงงานให้ company ดูเฉพาะบริษัทนั้น """
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, company_id=None):
        if company_id is not None:
            company = Company.objects.get(id=company_id)
            job_positions = JobPosition.objects.filter(company=company)
            serializer = JobPositionSerializer(job_positions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        company = Company.objects.get(user=request.user)
        job_positions = JobPosition.objects.filter(company=company)
        serializer = JobPositionSerializer(job_positions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
            serializer = JobPositionSerializer(data=request.data)
            if serializer.is_valid():
                    company = Company.objects.get(user=request.user)
                    serializer.save(company=company)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobPositionDetailView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        job_position = JobPosition.objects.get(pk=pk)
        serializer = JobPositionSerializer(job_position)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        job_position = JobPosition.objects.get(pk=pk)
        serializer = JobPositionSerializer(job_position, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job_position = JobPosition.objects.get(pk=pk)
        job_position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SkillView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SkillSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JobCategoryView(APIView):
    def get(self, request):
        categories = JobCategory.objects.all()
        serializer = JobCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobCategorySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
