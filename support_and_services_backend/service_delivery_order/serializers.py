from rest_framework import serializers
from .models import DeliveryOrder
from service_order.models import ServiceOrder
from connection.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id']

class ServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = ['service_order_id']

class DeliveryOrderSerializer(serializers.ModelSerializer):
    service_order_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceOrder.objects.all(), source="service_order", write_only=True
    )
    service_order = ServiceOrderSerializer(read_only=True)   

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)   

    class Meta:
        model = DeliveryOrder
        fields = "__all__"
