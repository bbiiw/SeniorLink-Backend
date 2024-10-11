from django.urls import path
from .views import ApplicantRegisterView, CompanyRegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/applicant/', ApplicantRegisterView.as_view(), name='register_applicant'),
    path('register/company/', CompanyRegisterView.as_view(), name='register_company'),
    path('login/<str:role>/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
