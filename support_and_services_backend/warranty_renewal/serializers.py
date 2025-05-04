from rest_framework import serializers
from .models import WarrantyRenewal
from service_contract.models import ServiceContract
from service_call.models import ServiceCall
from connection.models import *
from service_ticket.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMasterData
        fields = ['item_id', 'item_name']

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class ServiceCallSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=ItemMasterData.objects.all(), source="product", write_only=True
    )
    product = ProductSerializer(read_only=True) 

    service_ticket_id = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(), source="service_ticket", write_only=True
    )
    service_ticket = TicketSerializer(read_only=True) 

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    class Meta:
        model = ServiceCall
        fields = ['service_call_id', 'product', 'product_id', 'customer', 'customer_id', 'service_ticket', 'service_ticket_id']   

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
