from rest_framework import serializers
from .models import ServiceContract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContract
        fields = "__all__"