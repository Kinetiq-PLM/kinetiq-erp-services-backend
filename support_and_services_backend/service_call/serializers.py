from rest_framework import serializers
from .models import ServiceCall

class ServiceCallSerializer(serializers.ModelSerializer):
    technician_name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCall
        fields = "__all__"

    def get_technician_name(self, obj):
        if obj.technician_id:
            return f"{obj.technician.first_name} {obj.technician.last_name}"
        return None