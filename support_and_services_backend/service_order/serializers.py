from rest_framework import serializers
from .models import ServiceOrder, ServiceOrderItem
from service_analysis.models import ServiceAnalysis
from connection.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id']

class ServiceAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAnalysis
        fields = ['analysis_id']

class ServiceOrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    analysis_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceAnalysis.objects.all(), source="analysis", write_only=True
    )
    analysis = ServiceAnalysisSerializer(read_only=True)  

    class Meta:
        model = ServiceOrder
        fields = "__all__"

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"

class ItemMasterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMasterData
        fields = "__all__"

class InventoryItemMDSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=ItemMasterData.objects.all(), source="item", write_only=True
    )
    item = ItemMasterDataSerializer(read_only=True)  
    warehouse_id = serializers.PrimaryKeyRelatedField(
        queryset=Warehouse.objects.all(), source="warehouse", write_only=True, required=False, allow_null=True
    )
    warehouse = WarehouseSerializer(read_only=True) 

    class Meta:
        model = InventoryItemMD
        fields = "__all__"

class PrincipalItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalItem
        fields = "__all__"

class ServiceOrderItemSerializer(serializers.ModelSerializer):
    service_order_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceOrder.objects.all(), source="service_order", write_only=True
    )
    service_order = ServiceOrderSerializer(read_only=True)  

    item_id = serializers.PrimaryKeyRelatedField(
        queryset=InventoryItemMD.objects.all(), source="item", write_only=True
    )
    item = InventoryItemMDSerializer(read_only=True)  

    principal_item_id = serializers.PrimaryKeyRelatedField(
        queryset=PrincipalItem.objects.all(), source="principal_item", write_only=True, required=False, allow_null=True
    )
    principal_item = PrincipalItemSerializer(read_only=True)  

    warehouse_id = serializers.PrimaryKeyRelatedField(
        queryset=Warehouse.objects.all(), source="warehouse", write_only=True, required=False, allow_null=True
    )
    warehouse = WarehouseSerializer(read_only=True)  

    class Meta:
        model = ServiceOrderItem
        fields = "__all__"

