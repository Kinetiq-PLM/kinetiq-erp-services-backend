from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

after_analysis_router = DefaultRouter()
after_analysis_router.register(r'', AfterAnalysisViewSet, basename='after-analysis')

urlpatterns = after_analysis_router.urls + [
    path('analysis/<str:analysis_id>/', get_after_analysis, name='get-after-analysis')
]
