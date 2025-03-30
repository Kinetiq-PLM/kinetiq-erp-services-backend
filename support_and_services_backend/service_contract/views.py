from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import ServiceContract
from .serializers import ContractSerializer

@api_view(['GET'])
def get_contracts(request, product_id, customer_id):
    """get contracts filtered by product_id and customer_id"""
    contracts = ServiceContract.objects.filter(product_id=product_id, customer_id=customer_id)
    serializer = ContractSerializer(contracts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
