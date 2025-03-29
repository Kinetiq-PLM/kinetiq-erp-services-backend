from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceCallViewSet, create_service_call

call_router = DefaultRouter()
call_router.register(r'service-calls', ServiceCallViewSet, basename='service-call')

urlpatterns = call_router.urls + [
    path('queue-call', create_service_call, name='service-call-create'),
]