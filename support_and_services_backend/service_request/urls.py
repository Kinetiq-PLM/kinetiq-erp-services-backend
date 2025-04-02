from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet, create_service_request, update_service_request, get_filtered_requests

request_router = DefaultRouter()
request_router.register(r'service-requests', ServiceRequestViewSet, basename='service-request')

urlpatterns = request_router.urls + [
    path('create-request/', create_service_request, name='create-request'),
    path('service-requests/<str:service_request_id>/update/', update_service_request, name='update-service-request'),
    path('service-requests/<str:service_call_id>/call/', get_filtered_requests, name='get-service-request'),
]