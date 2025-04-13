from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

analysis_router = DefaultRouter()
analysis_router.register(r'service-analyses', ServiceAnalysisViewSet, basename='service-analysis')

urlpatterns = analysis_router.urls  + [
    path('service-analyses/<str:service_analysis_id>/', get_service_analysis, name='analysis-detail'),
    path('service-analyses/<str:analysis_id>/update/', update_service_analysis, name='update-analysis'),
    path('analyses-billing/<str:service_request_id>/', get_filtered_analyses, name='filtered-analyses'),
]