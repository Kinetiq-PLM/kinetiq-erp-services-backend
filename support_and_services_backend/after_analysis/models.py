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
    technician = models.ForeignKey('connection.Employee', on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    service_status = models.CharField(max_length=20, choices=ServiceStatusEnum.choices, default=ServiceStatusEnum.SCHEDULED)

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