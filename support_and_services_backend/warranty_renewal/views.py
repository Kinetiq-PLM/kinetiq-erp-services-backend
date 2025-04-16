from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WarrantyRenewal
from .serializers import WarrantyRenewalSerializer
from django.shortcuts import get_object_or_404

class WarrantyRenewalViewSet(ModelViewSet):
    queryset = WarrantyRenewal.objects.all()
    serializer_class = WarrantyRenewalSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all warranty renewals """
        queryset = self.get_queryset()
        serializer = WarrantyRenewalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_filtered_renewal(request, service_call_id): 
    """get renewals filtered by service_call_id"""
    renewals = WarrantyRenewal.objects.filter(service_call_id=service_call_id)
    serializer = WarrantyRenewalSerializer(renewals, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_filtered_renewal_tech(request, technician_id):
    """Get all employees with tech id"""
    renewals = WarrantyRenewal.objects.filter(service_call__technician_id=technician_id)  
    serializer = WarrantyRenewalSerializer(renewals, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)