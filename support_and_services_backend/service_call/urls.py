from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

call_router = DefaultRouter()
call_router.register(r'', ServiceCallViewSet, basename='service-call')

urlpatterns = call_router.urls + [
    path('calls/technicians/', get_technicians, name='get-technicians'),
    path('calls/products/', get_products, name='get-products'),
    # path('calls/update/<str:service_call_id>/', update_service_call, name='update-service-call'),
    path('ticket/<str:service_ticket_id>/', get_filtered_calls, name='get-service-call'),
]