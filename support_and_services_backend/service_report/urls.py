from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceReportViewSet, get_filtered_report_tech

report_router = DefaultRouter()
report_router.register(r'', ServiceReportViewSet, basename='service-report')

urlpatterns = report_router.urls + [
    path('reports/technician/<str:technician_id>/', get_filtered_report_tech, name='filtered-report-tech'),
]