from rest_framework import serializers
from connection.models import Customer, Employee
from .models import Ticket

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'email_address', 'phone_number', 'address_line1', 'address_line2']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name']

class TicketSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True
    )
    customer = CustomerSerializer(read_only=True)  
    salesrep_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='salesrep', write_only=True
    )
    salesrep = EmployeeSerializer(read_only=True)  

    class Meta:
        model = Ticket
        fields = "__all__"