from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import ServiceCall
from connection.models import Employee, ItemMasterData, Users
from .serializers import *
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
    
@api_view(['GET'])
def get_support_specialist(request):
    """Get all employees with position title 'Support Specialist'"""
    technicians = Employee.objects.filter(position__position_id='REG-2504-d563')  
    serializer = EmployeeSerializer(technicians, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_field_techs(request):
    """Get all employees with position title 'Field Service Technician'"""
    technicians = Employee.objects.filter(position__position_id='REG-2504-955e')  
    serializer = EmployeeSerializer(technicians, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_help_desk_agents(request):
    """Get all employees with position title 'Help Desk Agent'"""
    technicians = Employee.objects.filter(position__position_id='REG-2504-51bd')  
    serializer = EmployeeSerializer(technicians, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_mat_planners(request):
    """Get all employees with position title 'Materials Planner'"""
    employees = Employee.objects.filter(position__position_id='REG-2504-35c9')  
    users = Users.objects.filter(employee_id__in=employees)
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_management_employees(request):
    """Get all management employees with correct pos IDs"""
    position_ids = ['REG-2504-64ac', 'REG-2504-8228', 'REG-2504-d211']
    employees = Employee.objects.filter(position__position_id__in=position_ids)
    users = Users.objects.filter(employee_id__in=employees)
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_distrib_manager(request):
    """Get all distrib manager"""
    employees = Employee.objects.filter(position__position_id='REG-2504-d503')  
    users = Users.objects.filter(employee_id__in=employees)
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_technicians(request):
    """get all the employees"""
    technicians = Employee.objects.all()  
    serializer = EmployeeSerializer(technicians, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_products(request):
    """get all the products"""
    products = ItemMasterData.objects.all()  
    serializer = ItemMasterDataSerializer(products, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_filtered_calls(request, service_ticket_id):
    """get calls filtered by ticket id"""
    service_calls = ServiceCall.objects.filter(service_ticket_id=service_ticket_id)
    serializer = ServiceCallSerializer(service_calls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_filtered_calls_tech(request, technician_id):
    """get calls filtered by technician_id"""
    calls = ServiceCall.objects.filter(technician_id=technician_id)
    serializer = ServiceCallSerializer(calls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_filtered_user_tech(request, employee_id):
    """get user based on employee id"""
    user = Users.objects.get(employee_id=employee_id)
    serializer = UsersSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)