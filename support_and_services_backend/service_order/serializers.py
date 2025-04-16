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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'selling_price']

class ProductDocuSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )
    product = ProductSerializer(read_only=True)  

    class Meta:
        model = ProductDocumentItem
        fields = "__all__"

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = "__all__"

class InventoryItemMDSerializer(serializers.ModelSerializer):
    productdocu_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductDocumentItem.objects.all(), source="productdocu", write_only=True
    )
    productdocu = ProductDocuSerializer(read_only=True)  

    material_id = serializers.PrimaryKeyRelatedField(
        queryset=RawMaterial.objects.all(), source="material", write_only=True
    )
    material = RawMaterialSerializer(read_only=True)  

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

    class Meta:
        model = ServiceOrderItem
        fields = "__all__"

