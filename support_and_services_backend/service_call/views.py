from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceCall
from connection.models import Employee, Product
from .serializers import ServiceCallSerializer, EmployeeSerializer, ProductSerializer

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
    """get all the employee_ids"""
    technicians = Employee.objects.all()  
    serializer = EmployeeSerializer(technicians, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_products(request):
    """get all the products"""
    products = Product.objects.all()  
    serializer = ProductSerializer(products, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 