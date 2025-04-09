from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

delivery_order_router = DefaultRouter()
delivery_order_router.register(r'delivery-order', DeliveryOrderViewSet, basename='delivery-order')

urlpatterns = delivery_order_router.urls + [
    path('delivery-orders/<str:service_order_id>/', get_delivery_order, name='get-delivery-order'),
    path('delivery-order/<str:delivery_order_id>/update/', update_delivery_order, name='update-delivery-order'),
]
