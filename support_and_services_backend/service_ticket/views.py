from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Ticket
from .serializers import TicketSerializer, CustomerSerializer
from rest_framework.decorators import api_view
from datetime import datetime
from connection.models import Customer

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all tix """
        status_filter = request.query_params.get('status', None)
        priority_filter = request.query_params.get('priority', None)

        queryset = self.get_queryset()  

        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)

        serializer = TicketSerializer(queryset, many=True)  
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # submit tix
    def create(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        
        if serializer.is_valid():
            ticket = serializer.save(status='Open')  
            return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_ticket(request, ticket_id):
    """Fetches a single ticket"""
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)

    response_data = {
        "ticket_id": ticket.ticket_id,
        "status": ticket.status,
        "priority": ticket.priority,
        "created_at": ticket.created_at.strftime('%y/%m/%d') if isinstance(ticket.created_at, datetime) else None,
        "subject": ticket.subject,
        "description": ticket.description,
        "customer": {
            "customer_id": ticket.customer.customer_id,
            "name": ticket.customer.name,
            "email_address": ticket.customer.email_address,
            "phone_number": ticket.customer.phone_number,
        } if ticket.customer else None
    }
    
    return Response(response_data)

@api_view(['GET'])
def get_customers(request):
    """get all the customers"""
    customer = Customer.objects.all()  
    serializer = CustomerSerializer(customer, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['PATCH'])
def update_ticket(request, ticket_id):
    """updates a service ticket partially"""
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    
    serializer = TicketSerializer(ticket, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)