from django.db import models  

class AddsService(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."additional_service"'

    additional_service_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class AddsServiceType(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."additional_service_type"'
    
    additional_service_type_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    additional_service = models.ForeignKey(AddsService, on_delete=models.CASCADE)
    service_type = models.TextField()
    service_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    duration = models.IntegerField(default=1)
    date_start = models.DateField(auto_now=True)
    status = models.TextField()
    total_service_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False)