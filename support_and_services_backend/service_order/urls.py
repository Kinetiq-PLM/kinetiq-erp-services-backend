from django.urls import path
from .views import *

urlpatterns = [
    path('orders/<str:analysis_id>/', get_order, name='get-order'),
    path('order-items/<str:service_order_id>/', get_order_items, name='get-order-items'),
]