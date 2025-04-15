from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import ServiceOrder, ServiceOrderItem
from .serializers import *
from django.shortcuts import get_object_or_404
from connection.models import ItemMasterData, PrincipalItem, InventoryItemMD
from rest_framework.viewsets import ModelViewSet

class ServiceOrderViewSet(ModelViewSet):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer

    # create order
    def create(self, request, *args, **kwargs):
        serializer = ServiceOrderSerializer(data=request.data)
        
        if serializer.is_valid():
            service_order = serializer.save()  
            return Response(ServiceOrderSerializer(service_order).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceOrderItemViewSet(ModelViewSet):
    queryset = ServiceOrderItem.objects.all()
    serializer_class = ServiceOrderItemSerializer

    # create order item
    def create(self, request, *args, **kwargs):
        serializer = ServiceOrderItemSerializer(data=request.data)
        
        if serializer.is_valid():
            service_order_item = serializer.save()  
            return Response(ServiceOrderItemSerializer(service_order_item).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_order(request, analysis_id):
    """get single order data from service analysis"""
    service_orders = ServiceOrder.objects.filter(analysis_id=analysis_id)
    serializer = ServiceOrderSerializer(service_orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_order_items(request, service_order_id):
    """get order item list from order id"""
    service_order_items = ServiceOrderItem.objects.filter(service_order_id=service_order_id)
    serializer = ServiceOrderItemSerializer(service_order_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_items(request):
    """get all items"""
    item = ItemMasterData.objects.all()  
    serializer = ItemSerializer(item, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_principal_items(request, service_order_item_id):
    """get all principal items filtered by service order item id"""
    items = PrincipalItem.objects.filter(service_order_item_id=service_order_item_id)  
    serializer = PrincipalItemSerializer(items, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_inventory_items(request):
    """get all items from inventory"""
    item = InventoryItemMD.objects.all()  
    serializer = InventoryItemMDSerializer(item, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 