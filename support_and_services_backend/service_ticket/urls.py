from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, get_ticket, get_customers

ticket_router  = DefaultRouter()
ticket_router .register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns = ticket_router.urls + [
    path('tickets/<str:ticket_id>/', get_ticket, name='ticket-detail'), 
    path('customers/', get_customers, name='customers'), 
]