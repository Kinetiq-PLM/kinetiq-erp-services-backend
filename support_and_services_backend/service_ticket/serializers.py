# from rest_framework import serializers
# from connection.models import Customer, Technician
# from .models import Ticket

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['customer_id', 'name', 'email_address', 'phone_number', 'address_line1', 'address_line2']

# class TechnicianSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Technician
#         fields = ['technician_id', 'first_name', 'last_name']

# class TicketSerializer(serializers.ModelSerializer):
#     created_at = serializers.DateTimeField(read_only=True)

#     customer_id = serializers.PrimaryKeyRelatedField(
#         queryset=Customer.objects.all(), source='customer', write_only=True
#     )
#     technician_id = serializers.PrimaryKeyRelatedField(
#         queryset=Technician.objects.all(), source='salesrep', write_only=True
#     )

#     customer = CustomerSerializer(read_only=True)  
#     salesrep = TechnicianSerializer(read_only=True)  

#     class Meta:
#         model = Ticket
#         fields = [
#             'ticket_id', 'status', 'priority', 'created_at', 
#             'subject', 'description', 'customer', 'salesrep',
#             'customer_id', 'technician_id'  
#         ]