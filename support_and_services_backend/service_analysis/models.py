from django.db import models
from service_contract.models import ServiceContract
from service_request.models import ServiceRequest

class AnalysisStatusEnum(models.TextChoices):
    SCHEDULED = 'Scheduled'
    DONE = 'Done'

class ServiceAnalysis(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."service_analysis"'

    analysis_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    analysis_date = models.DateField(blank=True, null=True)
    technician = models.ForeignKey('connection.Employee', on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    analysis_status = models.CharField(max_length=20, choices=AnalysisStatusEnum.choices,  default=AnalysisStatusEnum.SCHEDULED)
    analysis_description = models.TextField(blank=True, null=True)
    product = models.ForeignKey('connection.ItemMasterData', on_delete=models.CASCADE)
    contract = models.ForeignKey(ServiceContract, on_delete=models.CASCADE)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 

