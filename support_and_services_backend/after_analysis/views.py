from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import AfterAnalysis
from .serializers import AfterAnalysisSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class AfterAnalysisViewSet(ModelViewSet):
    queryset = AfterAnalysis.objects.all()
    serializer_class = AfterAnalysisSerializer

    # create analysis
    def create(self, request, *args, **kwargs):
        serializer = AfterAnalysisSerializer(data=request.data)
        
        if serializer.is_valid():
            analysis_sched = serializer.save()  
            return Response(AfterAnalysisSerializer(analysis_sched).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_after_analysis(request, analysis_id):
    """get single after analysis from service analysis"""
    analysis_sched = get_object_or_404(AfterAnalysis, analysis_id=analysis_id)
    serializer = AfterAnalysisSerializer(analysis_sched)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_after_analysis(request, analysis_sched_id):
    """updates a after analysis partially"""
    analysis_sched = get_object_or_404(AfterAnalysis, analysis_sched_id=analysis_sched_id)
    serializer = AfterAnalysisSerializer(analysis_sched, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)