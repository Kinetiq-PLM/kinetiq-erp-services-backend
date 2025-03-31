from rest_framework import serializers
from .models import ServiceContract
from connection.models import Customer, Product, RenewalWarranty , AddsService, AddsServiceType

class AddServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddsServiceType
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'email_address', 'phone_number']

class AddsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddsService
        fields = ['additional_service_id']   

class RenewalWarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = RenewalWarranty
        fields = "__all__" 

class ContractSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )
    product = ProductSerializer(read_only=True)  

    additional_service_id = serializers.PrimaryKeyRelatedField(
        queryset=AddsService.objects.all(), source="additional_service", write_only=True
    )
    additional_service = AddsServiceSerializer(read_only=True) 

    renewal_id = serializers.PrimaryKeyRelatedField(
        queryset=RenewalWarranty.objects.all(), source="renewal", write_only=True
    )
    renewal = RenewalWarrantySerializer(read_only=True) 

    class Meta:
        model = ServiceContract
        fields = "__all__"