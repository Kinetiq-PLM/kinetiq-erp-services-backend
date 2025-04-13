from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

order_item_router = DefaultRouter()
order_item_router.register(r'service-order-item', ServiceOrderItemViewSet, basename='service-order-item')
order_item_router.register(r'service-order', ServiceOrderViewSet, basename='service-order')

urlpatterns = order_item_router.urls + [
    path('orders/<str:analysis_id>/', get_order, name='get-order'),
    path('order-items/<str:service_order_id>/', get_order_items, name='get-order-items'),
    path('items/', get_items, name='get-items'),
    path('principal-items/<str:service_order_item_id>/', get_principal_items, name='get-principal-items'),
    path('inventory-items/', get_inventory_items, name='inventory-items'),
    path('order-item/<str:service_order_item_id>/update/', update_order_item, name='inventory-items'),
]
