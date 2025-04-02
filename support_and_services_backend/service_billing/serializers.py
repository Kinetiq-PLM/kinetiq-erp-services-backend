from rest_framework import serializers
from .models import ServiceBilling

class ServiceBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBilling
        fields = "__all__"