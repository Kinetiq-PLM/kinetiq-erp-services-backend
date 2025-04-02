from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from django.shortcuts import get_object_or_404

class ServiceRequestViewSet(ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all requests """
        queryset = self.get_queryset()
        serializer = ServiceRequestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_service_request(request):
    """create service request"""
    serializer = ServiceRequestSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #print(serializer.errors) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_service_request(request, service_request_id):
    """updates a service request partially"""
    service_request = get_object_or_404(ServiceRequest, service_request_id=service_request_id)
    
    serializer = ServiceRequestSerializer(service_request, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_filtered_requests(request, service_call_id):
    """get requests filtered by call id"""
    service_requests = ServiceRequest.objects.filter(service_call_id=service_call_id)
    serializer = ServiceRequestSerializer(service_requests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

