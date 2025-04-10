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
def get_warranty_renewal(request, renewal_id):
    """Fetches a single warranty renewal"""
    renewal = get_object_or_404(WarrantyRenewal, renewal_id=renewal_id)
    serializer = WarrantyRenewalSerializer(renewal)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_warranty_renewal(request):
    """create warranty renewal"""
    serializer = WarrantyRenewalSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #print(serializer.errors) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_warranty_renewal(request, renewal_id):
    """updates a service request partially"""
    renewal = get_object_or_404(WarrantyRenewal, renewal_id=renewal_id)
    serializer = WarrantyRenewalSerializer(renewal, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_filtered_renewal(request, service_call_id): 
    """get renewals filtered by service_call_id"""
    renewals = WarrantyRenewal.objects.filter(service_call_id=service_call_id)
    serializer = WarrantyRenewalSerializer(renewals, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
