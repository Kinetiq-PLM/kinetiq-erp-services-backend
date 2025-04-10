from django.db import models
from service_analysis.models import ServiceAnalysis

class ServiceStatusEnum(models.TextChoices):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    IN_PROGRESS = "In Progress"

class AfterAnalysis(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."after_analysis_sched"'

    analysis_sched_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    analysis = models.ForeignKey(ServiceAnalysis, on_delete=models.CASCADE)
    service_date = models.DateField(null=False) 
    technician = models.ForeignKey('connection.Employee', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    service_status = models.CharField(max_length=20, choices=ServiceStatusEnum.choices, default=ServiceStatusEnum.SCHEDULED)
