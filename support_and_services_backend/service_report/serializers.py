from rest_framework import serializers
from .models import ServiceReport
from connection.models import *
from service_ticket.models import Ticket
from service_request.models import ServiceRequest
from service_billing.models import ServiceBilling
from service_call.models import ServiceCall

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'email_address', 'phone_number']

class TicketSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    customer = CustomerSerializer(read_only=True)  

    class Meta:
        model = Ticket
        fields = ['ticket_id', 'subject', 'description' , 'customer', 'customer_id', 'status']

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['service_request_id', 'request_type']

class RenewalWarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = RenewalWarranty
        fields = "__all__" 

class ServiceCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCall
        fields = ['service_call_id']   

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name']

class ServiceBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBilling
        fields = ['service_billing_id', 'total_payable']

class ServiceReportSerializer(serializers.ModelSerializer):
    service_ticket_id = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(), source='service_ticket', write_only=True
    )
    service_request_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceRequest.objects.all(), source='service_request', write_only=True
    )
    renewal_id = serializers.PrimaryKeyRelatedField(
        queryset=RenewalWarranty.objects.all(), source="renewal", write_only=True, required=False, allow_null=True
    )
    service_call_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCall.objects.all(), source='service_call', write_only=True
    )
    service_billing_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceBilling.objects.all(), source='service_billing', write_only=True, required=False, allow_null=True
    )
    technician_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source="technician", write_only=True
    ) 

    service_ticket = TicketSerializer(read_only=True) 
    service_request = ServiceRequestSerializer(read_only=True) 
    renewal = RenewalWarrantySerializer(read_only=True) 
    service_call = ServiceCallSerializer(read_only=True)
    service_billing = ServiceBillingSerializer(read_only=True)
    technician = EmployeeSerializer(read_only=True) 

    class Meta:
        model = ServiceReport
        fields = "__all__"


