from rest_framework import serializers
from .models import ServiceBilling
from connection.models import Customer, OpCost
from service_call.models import ServiceCall
from service_request.models import ServiceRequest
from warranty_renewal.models import WarrantyRenewal
from service_analysis.models import ServiceAnalysis
from service_order.models import ServiceOrder

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class ServiceCallSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    class Meta:
        model = ServiceCall
        fields = ['service_call_id', 'customer', 'customer_id']

class ServiceRequestSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    class Meta:
        model = ServiceRequest
        fields = ['service_request_id', 'customer', 'customer_id', 'request_type']

class WarrantyRenewalSerializer(serializers.ModelSerializer):
    service_call_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCall.objects.all(), source="service_call", write_only=True
    )
    service_call = ServiceCallSerializer(read_only=True) 

    class Meta:
        model = WarrantyRenewal
        fields = ['renewal_id', 'service_call', 'service_call_id', 'renewal_fee']

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAnalysis
        fields = ['analysis_id', 'labor_cost']

class ServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = ['service_order_id', 'order_total_price']        

class OpCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpCost
        fields = "__all__"     

class ServiceBillingSerializer(serializers.ModelSerializer):
    service_request_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceRequest.objects.all(), source="service_request", write_only=True, required=False, allow_null=True
    )
    service_request = ServiceRequestSerializer(read_only=True)  

    renewal_id = serializers.PrimaryKeyRelatedField(
        queryset=WarrantyRenewal.objects.all(), source="renewal", write_only=True, required=False, allow_null=True
    )
    renewal = WarrantyRenewalSerializer(read_only=True)  

    analysis_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceAnalysis.objects.all(), source="analysis", write_only=True, required=False, allow_null=True
    )
    analysis = AnalysisSerializer(read_only=True)  

    service_order_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceOrder.objects.all(), source="service_order", write_only=True, required=False, allow_null=True
    )
    service_order = ServiceOrderSerializer(read_only=True)  

    operational_cost_id = serializers.PrimaryKeyRelatedField(
        queryset=OpCost.objects.all(), source="operational_cost", write_only=True, required=False, allow_null=True
    )
    operational_cost = OpCostSerializer(read_only=True)  

    class Meta:
        model = ServiceBilling
        fields = "__all__"