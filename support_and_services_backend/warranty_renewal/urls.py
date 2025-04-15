from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
renewal_router = DefaultRouter()
renewal_router.register(r'', WarrantyRenewalViewSet, basename='warranty-renewals')

urlpatterns = renewal_router.urls + [
     path('call/<str:service_call_id>/', get_filtered_renewal, name='filtered-renewal'),
]