from django.db import models
from service_request.models import ServiceRequest
from service_analysis.models import ServiceAnalysis
from service_order.models import ServiceOrder

class BillStatusEnum(models.TextChoices):
    UNPAID = 'Unpaid'
    PAID = 'Paid'

class ServiceBilling(models.Model):
    class Meta:
        db_table = '"services"."service_billing"'

    service_billing_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    analysis = models.ForeignKey(ServiceAnalysis, on_delete=models.CASCADE)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service_order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE, blank=True, null=True)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    service_billing_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    outsource_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.0) # tatanong
    total_payable = models.DecimalField(max_digits=10, decimal_places=2, default=0.0) # ttrigger ata
    billing_status = models.CharField(max_length=20, choices=BillStatusEnum.choices,  default=BillStatusEnum.UNPAID)
    date_paid = models.DateField(blank=True, null=True)

