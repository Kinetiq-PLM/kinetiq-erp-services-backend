from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

after_analysis_router = DefaultRouter()
after_analysis_router.register(r'after-analysis', AfterAnalysisViewSet, basename='after-analysis')

urlpatterns = after_analysis_router.urls + [
    path('analysis-sched/<str:analysis_id>/', get_after_analysis, name='get-after-analysis'),
    path('analysis-sched/<str:analysis_sched_id>/update/', update_after_analysis, name='update-after-analysis'),
]
