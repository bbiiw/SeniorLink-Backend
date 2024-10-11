from django.urls import path
from .views import ApplicantProfileView

urlpatterns = [
    path('profile/', ApplicantProfileView.as_view(), name='applicant_profile'),
]
