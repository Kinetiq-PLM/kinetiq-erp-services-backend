from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service_ticket.urls import router

admin_router = DefaultRouter()
admin_router.registry.extend(router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("service_ticket.urls")),
]
