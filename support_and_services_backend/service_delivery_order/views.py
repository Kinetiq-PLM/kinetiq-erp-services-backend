from .models import DeliveryOrder
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers import DeliveryOrderSerializer
from rest_framework.viewsets import ModelViewSet

class DeliveryOrderViewSet(ModelViewSet):
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer

    # create order
    def create(self, request, *args, **kwargs):
        serializer = DeliveryOrderSerializer(data=request.data)
        
        if serializer.is_valid():
            delivery_order = serializer.save()  
            return Response(DeliveryOrderSerializer(delivery_order).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_delivery_order(request, service_order_id):
    """get single delivery order data from service order"""
    delivery_order = get_object_or_404(DeliveryOrder, service_order_id=service_order_id)
    serializer = DeliveryOrderSerializer(delivery_order)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_delivery_order(request, delivery_order_id):
    """updates a delivery order partially"""
    delivery_order = get_object_or_404(DeliveryOrder, delivery_order_id=delivery_order_id)
    serializer = DeliveryOrderSerializer(delivery_order, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)