from rest_framework import serializers
from .models import ServiceRequest
from connection.models import Customer, Employee
from service_call.models import ServiceCall

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id']

class ServiceCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCall
        fields = ['service_call_id']   

class ServiceRequestSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    service_call_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCall.objects.all(), source="service_call", write_only=True
    )
    service_call = ServiceCallSerializer(read_only=True)  

    technician_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source="technician", write_only=True
    )
    technician = EmployeeSerializer(read_only=True) 

    class Meta:
        model = ServiceRequest
        fields = "__all__"