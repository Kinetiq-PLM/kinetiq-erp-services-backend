from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

delivery_order_router = DefaultRouter()
delivery_order_router.register(r'', DeliveryOrderViewSet, basename='delivery-order')

urlpatterns = delivery_order_router.urls + [
    path('order/<str:service_order_id>/', get_delivery_order, name='get-delivery-order'),
    path('update/<str:delivery_order_id>/', update_delivery_order, name='update-delivery-order'),
]
