from django.db import models

class WarrantyRenewal(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."warranty_renewal"'

    renewal_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    service_call = models.ForeignKey('service_call.ServiceCall', on_delete=models.CASCADE, null=True, blank=True)
    contract = models.ForeignKey('service_contract.ServiceContract', on_delete=models.CASCADE, null=True, blank=True)
    duration = models.IntegerField(default=1)
    renewal_warranty_start = models.DateField(blank=True, null=True)
    renewal_warranty_end = models.DateField(blank=True, null=True)
    renewal_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True) 
