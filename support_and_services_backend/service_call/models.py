from django.db import models
from service_ticket.models import Ticket
from service_contract.models import ServiceContract

class CallTypeEnum(models.TextChoices):
    INQUIRY = 'Inquiry'
    REQUEST = 'Request'
    OTHER = 'Other'

class CallStatusEnum(models.TextChoices):
    OPEN = 'Open'
    CLOSED = 'Closed'
    IN_PROGRESS = 'In Progress'

class ServiceCall(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."service_call"'

    service_call_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    date_created = models.DateTimeField(auto_now_add=True)
    service_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    product = models.ForeignKey('connection.ItemMasterData', on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    call_type = models.CharField(max_length=20, choices=CallTypeEnum.choices, default=CallTypeEnum.INQUIRY)
    technician = models.ForeignKey('connection.Employee', on_delete=models.CASCADE)
    call_status = models.CharField(max_length=20, choices=CallStatusEnum.choices, default=CallStatusEnum.OPEN)
    date_closed = models.DateTimeField(null=True)
    contract = models.ForeignKey(ServiceContract, on_delete=models.CASCADE, null=True, blank=True)
    resolution = models.TextField(blank=True, null=True)
    priority_level = models.CharField(max_length=20, null=True)
    end_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if self.contract and self.contract.end_date:
            self.end_date = self.contract.end_date  

        super().save(*args, **kwargs) 

    