from django.db import models

class ContractStatusEnum(models.TextChoices):
    PENDING = "Pending"
    ACTIVE = "Active"
    EXPIRED = "Expired"
    TERMINATED = "Terminated"

class ServiceContract(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."service_contract"'

    contract_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    statement_item = models.ForeignKey('connection.StatementItem', on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('connection.Product', on_delete=models.CASCADE) 
    contract_description = models.TextField(blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True) # alr has a trigger
    end_date = models.DateField(blank=True, null=True) # alr has a trigger
    contract_status = models.CharField(max_length=20, choices=ContractStatusEnum.choices, default=ContractStatusEnum.PENDING)
    renewal = models.ForeignKey('connection.RenewalWarranty', on_delete=models.SET_NULL, blank=True, null=True)
    additional_service = models.ForeignKey('connection.AddsService', on_delete=models.SET_NULL, blank=True, null=True) 
    product_quantity = models.IntegerField(default=1) 
    renewal_date = models.DateField(blank=True, null=True) 
    renewal_end_date = models.DateField(blank=True, null=True) 

    def save(self, *args, **kwargs):
        if self.statement_item:
            if self.statement_item.product:
                self.product = self.statement_item.product  
            if self.statement_item.additional_service:
                self.additional_service = self.statement_item.additional_service  
            if self.statement_item.quantity:
                self.product_quantity = self.statement_item.quantity  

        if self.renewal:
            if self.renewal.renewal_warranty_start:
                self.renewal_date = self.renewal.renewal_warranty_start  
            if self.renewal.renewal_warranty_end:
                self.renewal_end_date = self.renewal.renewal_warranty_end  

        super().save(*args, **kwargs)
