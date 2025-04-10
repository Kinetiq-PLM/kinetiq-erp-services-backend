from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceBilling
from .serializers import ServiceBillingSerializer
from django.shortcuts import get_object_or_404

class ServiceBillingViewSet(ModelViewSet):
    queryset = ServiceBilling.objects.all()
    serializer_class = ServiceBillingSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all billings """
        queryset = self.get_queryset()
        serializer = ServiceBillingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

