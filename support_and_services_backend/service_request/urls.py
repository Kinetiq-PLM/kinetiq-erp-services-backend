from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import create_service_request

urlpatterns = [
    path('create-request/', create_service_request, name='create-request'),
]