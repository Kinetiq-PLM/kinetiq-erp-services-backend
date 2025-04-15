from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceBilling
from .serializers import *
from django.shortcuts import get_object_or_404
from connection.models import OpCost

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

@api_view(['GET'])
def get_all_op_costs(request):
    """Get all operational costs"""
    operational_costs = OpCost.objects.all()
    serializer = OpCostSerializer(operational_costs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_orders(request, analysis_id):
    """get orders data from service analysis"""
    service_orders = ServiceOrder.objects.filter(analysis_id=analysis_id)
    serializer = ServiceOrderSerializer(service_orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_filtered_bill_renewal(request, renewal_id): 
    """get billings filtered by renewal"""
    billings = ServiceBilling.objects.filter(renewal_id=renewal_id)
    serializer = ServiceBillingSerializer(billings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_filtered_bill_request(request, service_request_id): 
    """get billings filtered by renewal"""
    billings = ServiceBilling.objects.filter(service_request_id=service_request_id)
    serializer = ServiceBillingSerializer(billings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)