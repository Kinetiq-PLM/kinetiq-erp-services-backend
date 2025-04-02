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
    
@api_view(['GET'])
def get_call(request, service_call_id):
    """fetches a single service call"""
    service_call = get_object_or_404(ServiceCall, service_call_id=service_call_id)

    response_data = {
        "service_call_id": service_call.service_call_id,
        "date_created": service_call.date_created.strftime('%y/%m/%d') if isinstance(service_call.date_created, datetime) else None,
        "service_ticket":{
            "ticket_id": service_call.service_ticket.ticket_id,
            "subject": service_call.service_ticket.subject,
            "description": service_call.service_ticket.description,
        } if service_call.service_ticket else None,
        "product":{
            "product_id": service_call.product.product_id,
            "product_name": service_call.product.product_name,
        } if service_call.product else None,
        "customer": {
            "customer_id": service_call.customer.customer_id,
            "name": service_call.customer.name,
            "phone_number": service_call.customer.phone_number,
        } if service_call.customer else None,
        "call_type": service_call.call_type,
        "technician": service_call.technician,
        "call_status": service_call.call_status,
        "date_closed": service_call.date_closed,
        "contract": {
            "contract_id": service_call.contract.contract_id,
            "end_date": service_call.contract.end_date,
        } if service_call.contract else None,
        "resolution": service_call.resolution,
        "priority_level": service_call.priority_level,
    }
    
    return Response(response_data)

@api_view(['PATCH'])
def update_service_call(request, service_call_id):
    """updates a service call partially"""
    service_call = get_object_or_404(ServiceCall, service_call_id=service_call_id)
    
    serializer = ServiceCallSerializer(service_call, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_service_call(request):
    """queue a ticket (service call)"""
    serializer = ServiceCallSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #print(serializer.errors) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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