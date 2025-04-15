from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, get_customers

ticket_router  = DefaultRouter()
ticket_router.register(r'', TicketViewSet, basename='ticket')

urlpatterns = ticket_router.urls + [
    path('tickets/customers/', get_customers, name='customers')
]