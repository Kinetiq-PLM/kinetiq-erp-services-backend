from django.db import models
from service_call.models import ServiceCall

class RequestTypeEnum(models.TextChoices):
    REPAIR = "Repair"
    INSTALLATION = "Installation"
    MAINTENANCE = "Maintenance"
    OTHER = "Other"

class RequestStatusEnum(models.TextChoices):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    IN_PROGRESS = "In Progress"

class ServiceRequest(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."service_request"'

    service_request_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    service_call = models.ForeignKey(ServiceCall, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now=True)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    technician = models.ForeignKey('connection.Employee', on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=RequestTypeEnum.choices, null=False)
    request_status = models.CharField(max_length=50, choices=RequestStatusEnum.choices, null=False)
    request_description = models.TextField(blank=True, null=True) 
    request_remarks = models.TextField(blank=True, null=True) 
