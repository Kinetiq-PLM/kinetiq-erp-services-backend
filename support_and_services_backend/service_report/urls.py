from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceReportViewSet, get_service_report, get_renewals, create_service_report, update_service_report

report_router = DefaultRouter()
report_router.register(r'service-reports', ServiceReportViewSet, basename='service-report')

urlpatterns = report_router.urls + [
     path('service-reports/<str:service_report_id>/', get_service_report, name='report-detail'),
     path('renewals/', get_renewals, name='renewals'),
     path('create-report/', create_service_report, name='create-report'),
     path('service-reports/<str:report_id>/update/', update_service_report, name='update-report'),
]