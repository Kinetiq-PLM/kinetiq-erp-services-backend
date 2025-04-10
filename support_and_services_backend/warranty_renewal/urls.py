from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
renewal_router = DefaultRouter()
renewal_router.register(r'warranty-renewals', WarrantyRenewalViewSet, basename='warranty-renewals')

urlpatterns = renewal_router.urls + [
     path('warranty-renewal/<str:renewal_id>/', get_warranty_renewal, name='renewal-detail'),
     path('create-renewal/', create_warranty_renewal, name='create-renewal'),
     path('renewal/<str:renewal_id>/update/', update_warranty_renewal, name='update-renewal'),
     path('renewals/<str:service_call_id>/', get_filtered_renewal, name='filtered-renewal'),
]