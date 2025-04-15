from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import ServiceCall
from connection.models import Employee, Product
from .serializers import ServiceCallSerializer, EmployeeSerializer, ProductSerializer
from datetime import datetime

class ServiceCallViewSet(ModelViewSet):
    queryset = ServiceCall.objects.all()
    serializer_class = ServiceCallSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all calls """
        type_filter = request.query_params.get("call_type", None)
        status_filter = request.query_params.get("call_status", None)

        queryset = self.get_queryset()

        if type_filter:
            queryset = queryset.filter(call_type=type_filter)  
        if status_filter:
            queryset = queryset.filter(call_status=status_filter)  

        serializer = ServiceCallSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = ServiceCallSerializer(data=request.data)
        
        if serializer.is_valid():
            service_call = serializer.save()  
            return Response(ServiceCallSerializer(service_call).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['PATCH'])
# def update_service_call(request, service_call_id):
#     """updates a service call partially"""
#     service_call = get_object_or_404(ServiceCall, service_call_id=service_call_id)
    
#     serializer = ServiceCallSerializer(service_call, data=request.data, partial=True)  # partial allows partial update iykyk

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_technicians(request):
    """get all the employees"""
    technicians = Employee.objects.all()  
    serializer = EmployeeSerializer(technicians, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_products(request):
    """get all the products"""
    products = Product.objects.all()  
    serializer = ProductSerializer(products, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_filtered_calls(request, service_ticket_id):
    """get calls filtered by ticket id"""
    service_calls = ServiceCall.objects.filter(service_ticket_id=service_ticket_id)
    serializer = ServiceCallSerializer(service_calls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)