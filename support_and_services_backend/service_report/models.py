from django.db import models
from service_ticket.models import Ticket
from warranty_renewal.models import WarrantyRenewal
from service_request.models import ServiceRequest
from service_call.models import ServiceCall
from service_billing.models import ServiceBilling

class RepStatusEnum(models.TextChoices):
    DRAFT = 'Draft'
    SUBMITTED = 'Submitted'
    REVIEWED = 'Reviewed'

class ServiceReport(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."service_report"'

    report_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    service_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, blank=True, null=True)
    request_type = models.TextField(blank=True, null=True) 
    renewal = models.ForeignKey(WarrantyRenewal, on_delete=models.SET_NULL, blank=True, null=True)
    service_call = models.ForeignKey(ServiceCall, on_delete=models.CASCADE)
    service_billing = models.ForeignKey(ServiceBilling, on_delete=models.CASCADE, blank=True, null=True)
    technician = models.ForeignKey('connection.Employee', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    report_status = models.CharField(max_length=20, choices=RepStatusEnum.choices, default=RepStatusEnum.DRAFT)
    submission_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

