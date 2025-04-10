from rest_framework import serializers
from .models import WarrantyRenewal
from service_contract.models import ServiceContract
from service_call.models import ServiceCall

class ServiceCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCall
        fields = ['service_call_id']

class ServiceContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContract
        fields = ['contract_id']

class WarrantyRenewalSerializer(serializers.ModelSerializer):
    service_call_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCall.objects.all(), source="service_call", write_only=True
    )
    service_call = ServiceCallSerializer(read_only=True) 

    contract_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceContract.objects.all(), source="contract", write_only=True
    )
    contract = ServiceContractSerializer(read_only=True)  

    class Meta:
        model = WarrantyRenewal
        fields = "__all__"
