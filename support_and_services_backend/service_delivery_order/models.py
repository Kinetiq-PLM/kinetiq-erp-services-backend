from django.db import models
from service_order.models import ServiceOrder

class DelStatusEnum(models.TextChoices):
    PENDING = 'Pending'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'

class DeliveryOrder(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."delivery_order"'

    delivery_order_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    service_order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    customer_address = models.TextField(blank=True, null=True)
    delivery_status = models.CharField(max_length=20, choices=DelStatusEnum.choices,  default=DelStatusEnum.PENDING)
    delivery_date = models.DateField(auto_now=True)

