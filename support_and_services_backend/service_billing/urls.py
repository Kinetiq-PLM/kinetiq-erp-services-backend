from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

billing_router = DefaultRouter()
billing_router.register(r'', ServiceBillingViewSet, basename='service-billing')

urlpatterns = billing_router.urls + [
    path('billings/operational-costs/', get_all_op_costs, name='operational-costs'),
    path('orders/<str:analysis_id>/', get_orders, name='orders '),
    path('billing-renewals/<str:renewal_id>/', get_filtered_bill_renewal, name='filtered-bill-renewal'),
    path('billing-requests/<str:service_request_id>/', get_filtered_bill_request, name='filtered-bill-request'),
    path('billings/technician/<str:technician_id>/', get_filtered_bill_tech, name='filtered-bill-tech'),
]