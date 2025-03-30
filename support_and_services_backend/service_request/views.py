from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

@api_view(['POST'])
def create_service_request(request):
    """create service request"""
    serializer = ServiceRequestSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #print(serializer.errors) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
