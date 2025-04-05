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
def get_service_analysis(request, service_analysis_id):
    """Fetches a single service analysis"""
    analysis = get_object_or_404(ServiceAnalysis, service_analysis_id=service_analysis_id)
    serializer = ServiceAnalysisSerializer(analysis)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_service_analysis(request, analysis_id):
    """updates a service analysis partially"""
    analysis = get_object_or_404(ServiceAnalysis, analysis_id=analysis_id)
    
    serializer = ServiceAnalysisSerializer(analysis, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)