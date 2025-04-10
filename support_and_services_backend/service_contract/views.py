from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import ServiceContract
from warranty_renewal.models import WarrantyRenewal
from .serializers import ContractSerializer, AddServiceTypeSerializer, WarrantyRenewalSerializer, StatementItemSerializer
from connection.models import AddsServiceType, StatementItem
from django.shortcuts import get_object_or_404

class ServiceContractViewSet(ModelViewSet):
    queryset = ServiceContract.objects.all()
    serializer_class = ContractSerializer

    def list(self, request, *args, **kwargs):
        """ fetch all service contracts """
        queryset = self.get_queryset()
        serializer = ContractSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create contract
    def create(self, request, *args, **kwargs):
        serializer = ContractSerializer(data=request.data)
        
        if serializer.is_valid():
            contract = serializer.save()  
            return Response(ContractSerializer(contract).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_contracts(request, product_id, customer_id):
    """get contracts filtered by product_id and customer_id"""
    contracts = ServiceContract.objects.filter(product_id=product_id, customer_id=customer_id)
    serializer = ContractSerializer(contracts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_additional_service_list(request, additional_service_id):
    """get add service list from add service id"""
    additional_service_types = AddsServiceType.objects.filter(additional_service_id=additional_service_id)
    serializer = AddServiceTypeSerializer(additional_service_types, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_filtered_renewals(request, product_id, customer_id): # change to contract na ung magfifilter
    """get renewals filtered by product_id and customer_id"""
    contracts = WarrantyRenewal.objects.filter(product_id=product_id, customer_id=customer_id)
    serializer = WarrantyRenewalSerializer(contracts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_contract(request, contract_id):
    """updates a service contract partially"""
    contract = get_object_or_404(ServiceContract, contract_id=contract_id)
    serializer = ContractSerializer(contract, data=request.data, partial=True)  # partial allows partial update iykyk

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_statement_list(request):
    """get all statement items"""
    statement_item = StatementItem.objects.all()  
    serializer = StatementItemSerializer(statement_item, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 