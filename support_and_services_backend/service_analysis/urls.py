from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

analysis_router = DefaultRouter()
analysis_router.register(r'', ServiceAnalysisViewSet, basename='service-analysis')

urlpatterns = analysis_router.urls  + [
    path('request/<str:service_request_id>/', get_filtered_analyses, name='filtered-analyses'),
]