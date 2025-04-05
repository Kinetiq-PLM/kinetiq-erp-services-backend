from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import ServiceOrder, ServiceOrderItem
from .serializers import ServiceOrderSerializer, ServiceOrderItemSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_order(request, analysis_id):
    """get single order data from service analysis"""
    service_order = get_object_or_404(ServiceOrder, analysis_id=analysis_id)
    serializer = ServiceOrderSerializer(service_order)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_order_items(request, service_order_id):
    """get order item list from order id"""
    service_order_items = ServiceOrderItem.objects.filter(service_order_id=service_order_id)
    serializer = ServiceOrderItemSerializer(service_order_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)