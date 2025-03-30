from django.contrib import admin
from django.urls import path, include
from service_ticket.urls import ticket_router
from service_call.urls import call_router
from service_request.urls import request_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(ticket_router.urls)),  
    path("", include(call_router.urls)),
    path("", include(request_router.urls)),
    path("", include('service_call.urls')),
    path("", include('service_ticket.urls')),
    path("", include('service_contract.urls')),
    path("", include('service_request.urls')),
]