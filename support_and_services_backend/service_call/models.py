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
        db_table = '"services"."service_call"'

    service_call_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    date_created = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    product = models.ForeignKey('connection.Product', on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    call_type = models.CharField(max_length=20, choices=CallTypeEnum.choices, default=CallTypeEnum.INQUIRY)
    technician = models.ForeignKey('connection.Employee', on_delete=models.CASCADE)
    call_status = models.CharField(max_length=20, choices=CallStatusEnum.choices, default=CallStatusEnum.OPEN)
    date_closed = models.DateTimeField(null=True)
    contract = models.ForeignKey(ServiceContract, on_delete=models.CASCADE)
    resolution = models.TextField(blank=True, null=True)

    @property
    def end_date(self):
        # fetches end_date from contract_id
        return self.contract.end_date if self.contract else None

    @property
    def priority_level(self):
        # fetches prio_level from ticket_id
        return self.ticket.priority if self.ticket else None

    