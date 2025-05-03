from django.db import models


class ContractStatusEnum(models.TextChoices):
    PENDING = "Pending"
    ACTIVE = "Active"
    EXPIRED = "Expired"
    TERMINATED = "Terminated"

class ServiceContract(models.Model):
    from warranty_renewal.models import WarrantyRenewal
    class Meta:
        managed = False
        db_table = '"services"."service_contract"'

    contract_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    statement_item = models.ForeignKey('connection.StatementItem', on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('connection.ItemMasterData', on_delete=models.CASCADE) 
    contract_description = models.TextField(blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True) # alr has a trigger
    end_date = models.DateField(blank=True, null=True) # alr has a trigger
    contract_status = models.CharField(max_length=20, choices=ContractStatusEnum.choices, default=ContractStatusEnum.PENDING)
    renewal = models.ForeignKey(WarrantyRenewal, on_delete=models.SET_NULL, blank=True, null=True)
    additional_service = models.ForeignKey('connection.AddsService', on_delete=models.SET_NULL, blank=True, null=True) 
    product_quantity = models.IntegerField(default=1) 
    renewal_date = models.DateField(blank=True, null=True) 
    renewal_end_date = models.DateField(blank=True, null=True) 
