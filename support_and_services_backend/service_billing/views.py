from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceBilling
from .serializers import ServiceBillingSerializer
from django.shortcuts import get_object_or_404

class ServiceBillingViewSet(ModelViewSet):
    queryset = ServiceBilling.objects.all()
    serializer_class = ServiceBillingSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all billings """
        queryset = self.get_queryset()
        serializer = ServiceBillingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # create billing
    def create(self, request, *args, **kwargs):
        serializer = ServiceBillingSerializer(data=request.data)
        
        if serializer.is_valid():
            service_billing = serializer.save()  
            return Response(ServiceBillingSerializer(service_billing).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def update_contract(request, service_billing_id):
    """updates a service billing partially"""
    service_billing = get_object_or_404(ServiceBilling, service_billing_id=service_billing_id)
    serializer = ServiceBillingSerializer(service_billing, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)