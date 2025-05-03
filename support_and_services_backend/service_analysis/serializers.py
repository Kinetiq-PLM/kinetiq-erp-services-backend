from rest_framework import serializers
from connection.models import *
from service_request.models import ServiceRequest
from service_contract.models import ServiceContract
from .models import ServiceAnalysis

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['service_request_id', 'request_type']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name']

class ItemMasterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMasterData
        fields = ['item_id', 'item_name']

class ServiceContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContract
        fields = ['contract_id', 'end_date']

class ServiceAnalysisSerializer(serializers.ModelSerializer):
    service_request_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceRequest.objects.all(), source='service_request', write_only=True
    )
    contract_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceContract.objects.all(), source='contract', write_only=True, required=False, allow_null=True
    )
    technician_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source="technician", write_only=True
    ) 
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=ItemMasterData.objects.all(), source="product", write_only=True
    )
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )

    service_request = ServiceRequestSerializer(read_only=True) 
    contract = ServiceContractSerializer(read_only=True) 
    technician = EmployeeSerializer(read_only=True) 
    product = ItemMasterDataSerializer(read_only=True) 
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = ServiceAnalysis
        fields = "__all__"


