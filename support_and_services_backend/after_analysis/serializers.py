from rest_framework import serializers
from .models import AfterAnalysis
from service_analysis.models import ServiceAnalysis
from connection.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name']

class ServiceAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAnalysis
        fields = ['analysis_id']

class AfterAnalysisSerializer(serializers.ModelSerializer):
    technician_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source="technician", write_only=True, required=False, allow_null=True
    )
    technician = EmployeeSerializer(read_only=True) 

    analysis_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceAnalysis.objects.all(), source="analysis", write_only=True
    )
    analysis = ServiceAnalysisSerializer(read_only=True)  

    class Meta:
        model = AfterAnalysis
        fields = "__all__"


