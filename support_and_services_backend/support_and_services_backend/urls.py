from django.contrib import admin
from django.urls import path, include
from service_ticket.urls import ticket_router
from service_call.urls import call_router
from service_request.urls import request_router
from service_report.urls import report_router
from service_billing.urls import billing_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(ticket_router.urls)),  
    path("", include(call_router.urls)),
    path("", include(request_router.urls)),
    path("", include(report_router.urls)),
   path("", include(billing_router.urls)), 
    path("", include('service_call.urls')),
    path("", include('service_ticket.urls')),
    path("", include('service_contract.urls')),
    path("", include('service_request.urls')),
    path("", include('service_report.urls')),
]