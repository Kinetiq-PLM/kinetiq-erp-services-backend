from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer, CustomerSerializer
from rest_framework.decorators import api_view
from connection.models import Customer

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all tix """
        type_filter = request.query_params.get('type', 'Service')

        queryset = self.get_queryset()  

        if type_filter:
            queryset = queryset.filter(type=type_filter)

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
def get_customers(request):
    """get all the customers"""
    customer = Customer.objects.all()  
    serializer = CustomerSerializer(customer, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 