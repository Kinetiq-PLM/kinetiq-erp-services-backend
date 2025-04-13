from rest_framework import serializers
from .models import WarrantyRenewal
from service_contract.models import ServiceContract
from service_call.models import ServiceCall
from connection.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'selling_price']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class ServiceCallSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )
    product = ProductSerializer(read_only=True) 

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    class Meta:
        model = ServiceCall
        fields = ['service_call_id', 'product', 'product_id', 'customer', 'customer_id']

class ServiceContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContract
        fields = ['contract_id', 'contract_status']

class WarrantyRenewalSerializer(serializers.ModelSerializer):
    service_call_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCall.objects.all(), source="service_call", write_only=True
    )
    service_call = ServiceCallSerializer(read_only=True) 

    contract_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceContract.objects.all(), source="contract", write_only=True
    )
    contract = ServiceContractSerializer(read_only=True)  

    class Meta:
        model = WarrantyRenewal
        fields = "__all__"
