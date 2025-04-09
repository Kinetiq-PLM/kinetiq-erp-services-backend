from django.contrib import admin
from django.urls import path, include
from service_ticket.urls import ticket_router
from service_call.urls import call_router
from service_request.urls import request_router
from service_report.urls import report_router
from service_billing.urls import billing_router
from service_analysis.urls import analysis_router
from service_order.urls import order_item_router
from service_delivery_order.urls import delivery_order_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(ticket_router.urls)),  
    path("", include(call_router.urls)),
    path("", include(request_router.urls)),
    path("", include(report_router.urls)),
    path("", include(billing_router.urls)), 
    path("", include(analysis_router.urls)),
    path("", include(order_item_router.urls)),
    path("", include(delivery_order_router.urls)),
    path("", include('service_call.urls')),
    path("", include('service_ticket.urls')),
    path("", include('service_contract.urls')),
    path("", include('service_request.urls')),
    path("", include('service_report.urls')),
    path("", include('service_analysis.urls')),  
    path("", include('service_order.urls')),    
    path("", include('service_delivery_order.urls')),
]