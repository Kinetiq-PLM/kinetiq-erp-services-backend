from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceReport
from .serializers import ServiceReportSerializer, RenewalWarrantySerializer
from django.shortcuts import get_object_or_404
from connection.models import RenewalWarranty

class ServiceReportViewSet(ModelViewSet):
    queryset = ServiceReport.objects.all()
    serializer_class = ServiceReportSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all report """
        queryset = self.get_queryset()
        serializer = ServiceReportSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_service_report(request, service_report_id):
    """Fetches a single service report"""
    service_report = get_object_or_404(ServiceReport, service_report_id=service_report_id)
    serializer = ServiceReportSerializer(service_report)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_renewals(request):
    """get all the renewals"""
    renewals = RenewalWarranty.objects.all()  
    serializer = RenewalWarrantySerializer(renewals, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def create_service_report(request):
    """create report"""
    serializer = ServiceReportSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #print(serializer.errors) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_service_report(request, report_id):
    """updates a service request partially"""
    report = get_object_or_404(ServiceReport, report_id=report_id)
    
    serializer = ServiceReportSerializer(report, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)