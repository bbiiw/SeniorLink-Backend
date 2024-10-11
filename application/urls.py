from django.urls import path
from applicant.views import ApplicantProfileView
from company.views import CompanyProfileView
from .views import ApplicationListView, ApplyForJobView, StatusView, CompanyApplicationView, ApplicantApplicationView

urlpatterns = [
    path('status/', StatusView.as_view(), name='status'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/<int:id>/', ApplicationListView.as_view(), name='application-update'),

    path('applicant/applications/', ApplicantApplicationView.as_view(), name='applicant-applications'),
    path('applicant/applications/<int:application_id>/', ApplicantApplicationView.as_view(), name='applicant-update'),
    path('applicant/applications/profile/<int:company_id>/', CompanyProfileView.as_view(), name='company-profile'),

    path('company/applications/', CompanyApplicationView.as_view(), name='company-applications'),
    path('company/applications/<int:application_id>/', CompanyApplicationView.as_view(), name='company-update'),
    path('company/applications/profile/<int:applicant_id>/', ApplicantProfileView.as_view(), name='applicant-profile'),

    path('apply/<int:job_id>/', ApplyForJobView.as_view(), name='apply-for-job'),
]
