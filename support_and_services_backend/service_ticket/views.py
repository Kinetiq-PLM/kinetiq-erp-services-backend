# from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import Ticket
# from .serializers import TicketSerializer

# class TicketViewSet(ModelViewSet):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer

#     def retrieve(self, request, pk=None):
#         """fetches a single ticket"""
#         ticket = get_object_or_404(Ticket.objects.select_related('customer', 'salesrep'), ticket_id=pk)

#         response_data = {
#             "ticket": {
#                 "ticket_id": ticket.ticket_id,
#                 "status": ticket.status,
#                 "priority": ticket.priority,
#                 "created_at": ticket.created_at.strftime('%Y-%m-%d %H:%M:%S'),
#                 "subject": ticket.subject,
#                 "description": ticket.description,
#             },
#             "customer": {
#                 "customer_id": ticket.customer.customer_id,
#                 "name": ticket.customer.name,
#                 "email_address": ticket.customer.email_address,
#                 "phone_number": ticket.customer.phone_number,
#             },
#             "salesrep": {
#                 "technician_id": ticket.salesrep.technician_id,
#                 "name": f"{ticket.salesrep.first_name} {ticket.salesrep.last_name}"
#             }
#         }
#         return Response(response_data)
    
#     def create(self, request, *args, **kwargs):
#         """Submits a ticket."""
#         serializer = TicketSerializer(data=request.data)
        
#         if serializer.is_valid():
#             ticket = serializer.save(status='Open')  
#             return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
