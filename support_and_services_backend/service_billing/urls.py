from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceBillingViewSet

billing_router = DefaultRouter()
billing_router.register(r'service-billings', ServiceBillingViewSet, basename='service-billing')

urlpatterns = billing_router.urls 