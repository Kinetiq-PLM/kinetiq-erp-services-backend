from rest_framework import serializers
from .models import ServiceCall
from connection.models import Employee, Product

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ServiceCallSerializer(serializers.ModelSerializer):
    technician_name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCall
        fields = "__all__"

    def get_technician_name(self, obj):
        if obj.technician_id:
            return f"{obj.technician.first_name} {obj.technician.last_name}"
        return None