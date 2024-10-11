# urls.py
from django.urls import path
from .views import SkillView, JobCategoryView, JobPositionListView, JobPositionDetailView, AllJobPositionListView

urlpatterns = [
    path('skills/', SkillView.as_view(), name='skill'),
    path('job_category/', JobCategoryView.as_view(), name='jobcategory'),

    path('company_positions/', JobPositionListView.as_view(), name='company-job-positions'),
    path('company_positions/<int:company_id>/', JobPositionListView.as_view(), name='companyid-job-positions'),
    
    path('positions/', AllJobPositionListView.as_view(), name='applicant-job-positions'),
    path('positions/<int:pk>/', JobPositionDetailView.as_view(), name='jobposition-detail'),
]
