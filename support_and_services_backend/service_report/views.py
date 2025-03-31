from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceReport
from .serializers import ServiceReportSerializer
from django.shortcuts import get_object_or_404

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