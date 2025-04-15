from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceReportViewSet

report_router = DefaultRouter()
report_router.register(r'', ServiceReportViewSet, basename='service-report')

urlpatterns = report_router.urls 