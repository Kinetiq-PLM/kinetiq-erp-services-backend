from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceContractViewSet, get_contracts, get_additional_service_list, get_filtered_renewals, update_contract

contract_router = DefaultRouter()
contract_router.register(r'service-contracts', ServiceContractViewSet, basename='service-contract')

urlpatterns = contract_router.urls + [
    path('contracts/<str:product_id>/<str:customer_id>/', get_contracts, name='get_contracts'),
    path('contracts/<str:additional_service_id>/', get_additional_service_list, name='get_add_services'),
    path('renewals/<str:product_id>/<str:customer_id>/', get_filtered_renewals, name='get_renewals'),
    path('update-contract/<str:contract_id>/', update_contract, name='update-contract'),
]