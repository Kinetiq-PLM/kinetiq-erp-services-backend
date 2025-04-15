from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet, get_filtered_requests

request_router = DefaultRouter()
request_router.register(r'', ServiceRequestViewSet, basename='service-request')

urlpatterns = request_router.urls + [
    path('call/<str:service_call_id>/', get_filtered_requests, name='get-service-request'),
]