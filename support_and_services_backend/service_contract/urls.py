from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import get_contracts

urlpatterns = [
    path('contracts/<str:product_id>/<str:customer_id>/', get_contracts, name='get_contracts'),
]