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
    contract_description = models.TextField(blank=True, null=True)
    date_issued = models.DateField() # alr has a trigger
    end_date = models.DateField() # alr has a trigger
    contract_status = models.CharField(max_length=20, choices=ContractStatusEnum.choices, default=ContractStatusEnum.PENDING)
    renewal_bool = models.BooleanField(default=False)
    renewal = models.ForeignKey('connection.RenewalWarranty', on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def additional_service(self):
        # fetches additional_service from statement_item
        return self.statement_item.additional_service if self.statement_item else None
    
    @property
    def product(self):
        # fetches product from statement_item
        return self.statement_item.product if self.statement_item else None
    
    @property
    def product_quantity(self):
        # fetches product_quantity from statement_item
        return self.statement_item.quantity if self.statement_item else 1
    
    @property
    def renewal_date(self):
        # fetches renewal_warranty_start from renewal
        return self.renewal.renewal_warranty_start if self.renewal else None
    
    @property
    def renewal_end_date(self):
        # fetches renewal_warranty_end from renewal
        return self.renewal.renewal_warranty_end if self.renewal else None