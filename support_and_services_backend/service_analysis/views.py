from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import ServiceAnalysis
from .serializers import ServiceAnalysisSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class ServiceAnalysisViewSet(ModelViewSet):
    queryset = ServiceAnalysis.objects.all()
    serializer_class = ServiceAnalysisSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all analysis """
        queryset = self.get_queryset()
        serializer = ServiceAnalysisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = ServiceAnalysisSerializer(data=request.data)
        
        if serializer.is_valid():
            analysis = serializer.save()  
            return Response(ServiceAnalysisSerializer(analysis).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_filtered_analyses(request, service_request_id): 
    """Get the first analysis filtered by service_request_id"""
    analysis = ServiceAnalysis.objects.filter(service_request_id=service_request_id).first()
    
    if analysis is None:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServiceAnalysisSerializer(analysis)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_filtered_analyses_tech(request, technician_id):
    """Get all employees with tech id"""
    analyses = ServiceAnalysis.objects.filter(technician_id=technician_id)  
    serializer = ServiceAnalysisSerializer(analyses, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)