from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

billing_router = DefaultRouter()
billing_router.register(r'service-billings', ServiceBillingViewSet, basename='service-billing')

urlpatterns = billing_router.urls + [
    path('service-billing/<str:service_billing_id>/update/', update_billing, name='update-contract'),
    path('operational-costs/', get_all_op_costs, name='operational-costs'),
    path('orders/billings/<str:analysis_id>/', get_orders, name='orders '),
]