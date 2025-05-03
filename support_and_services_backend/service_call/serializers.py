from rest_framework import serializers
from .models import ServiceCall
from connection.models import Employee, ItemMasterData, Customer, Users
from service_ticket.models import Ticket
from service_contract.models import ServiceContract

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class ItemMasterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMasterData
        fields = ['item_id', 'item_name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['ticket_id', 'subject', 'description']

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContract
        fields = ['contract_id', 'end_date', 'contract_status']

class ServiceCallSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True
    )
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=ItemMasterData.objects.all(), source='product', write_only=True
    )
    service_ticket_id = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(), source='service_ticket', write_only=True
    )
    contract_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceContract.objects.all(), source='contract', write_only=True,
         required=False, allow_null=True
    )

    customer = CustomerSerializer(read_only=True)
    product = ItemMasterDataSerializer(read_only=True)  
    service_ticket = TicketSerializer(read_only=True) 
    contract = ContractSerializer(read_only=True) 

    class Meta:
        model = ServiceCall
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'employee_id']