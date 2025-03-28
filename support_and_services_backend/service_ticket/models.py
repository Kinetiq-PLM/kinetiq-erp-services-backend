from django.db import models  

class StatusEnum(models.TextChoices):
    OPEN = 'Open'
    IN_PROGRESS = 'In Progress'
    CLOSED = 'Closed'

class PriorityEnum(models.TextChoices):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    URGENT = 'Urgent'


class Ticket(models.Model):
    class Meta:
        managed = False
        db_table = '"sales"."ticket"'

    ticket_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    salesrep = models.ForeignKey('connection.Employee', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=StatusEnum.choices, default=StatusEnum.OPEN)
    priority = models.CharField(max_length=10, choices=PriorityEnum.choices, default=PriorityEnum.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)