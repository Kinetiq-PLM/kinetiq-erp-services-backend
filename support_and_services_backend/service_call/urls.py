from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

call_router = DefaultRouter()
call_router.register(r'service-calls', ServiceCallViewSet, basename='service-call')

urlpatterns = call_router.urls + [
    path('queue-call/', create_service_call, name='service-call-create'),
    path('technicians/', get_technicians, name='get-technicians'),
    path('products/', get_products, name='get-products'),
    path('service-calls/<str:service_call_id>/', get_call, name='call-detail'), 
    path('service-calls/<str:service_call_id>/update/', update_service_call, name='update-service-call'),
    path('service-calls/<str:service_ticket_id>/ticket/', get_filtered_calls, name='get-service-call'),
]