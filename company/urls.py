from django.urls import path
from .views import CompanyProfileView, CompanyCategoryView

urlpatterns = [
    path('profile/', CompanyProfileView.as_view(), name='company_profile'),
    path('company_category/', CompanyCategoryView.as_view(), name='company_category'),
]