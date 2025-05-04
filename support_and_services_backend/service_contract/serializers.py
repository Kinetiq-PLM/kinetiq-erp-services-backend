from rest_framework import serializers
from .models import ServiceContract
from warranty_renewal.models import WarrantyRenewal
from connection.models import *

class AddServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddsServiceType
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMasterData
        fields = ['item_id', 'item_name']

class InventoryItemSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=ItemMasterData.objects.all(), source="item", write_only=True
    )
    item = ProductSerializer(read_only=True)  
    class Meta:
        model = InventoryItemMD
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'email_address', 'phone_number']

class AddsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddsService
        fields = ['additional_service_id']   

class WarrantyRenewalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarrantyRenewal
        fields = "__all__" 

class StatementSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    class Meta:
        model = Statement
        fields = ['statement_id', 'customer', 'customer_id']   

class StatementItemSerializer(serializers.ModelSerializer):
    inventory_item_id = serializers.PrimaryKeyRelatedField(
        queryset=InventoryItemMD.objects.all(), source="inventory_item", write_only=True
    )
    inventory_item = InventoryItemSerializer(read_only=True)  

    statement_id = serializers.PrimaryKeyRelatedField(
        queryset=Statement.objects.all(), source="statement", write_only=True
    )
    statement = StatementSerializer(read_only=True) 

    class Meta:
        model = StatementItem
        fields = "__all__"

class ContractSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=ItemMasterData.objects.all(), source="product", write_only=True
    )
    product = ProductSerializer(read_only=True)  

    additional_service_id = serializers.PrimaryKeyRelatedField(
        queryset=AddsService.objects.all(), source="additional_service", write_only=True, allow_null=True
    )
    additional_service = AddsServiceSerializer(read_only=True) 

    renewal_id = serializers.PrimaryKeyRelatedField(
        queryset=WarrantyRenewal.objects.all(), source="renewal", write_only=True, required=False, allow_null=True
    )
    renewal = WarrantyRenewalSerializer(read_only=True) 

    statement_item_id = serializers.PrimaryKeyRelatedField(
        queryset=StatementItem.objects.all(), source="statement_item", write_only=True
    )
    statement_item = StatementItemSerializer(read_only=True) 

    class Meta:
        model = ServiceContract
        fields = "__all__"