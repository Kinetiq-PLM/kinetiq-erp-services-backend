from django.db import models
from service_analysis.models import ServiceAnalysis

class AnalysisStatusEnum(models.TextChoices):
    SCHEDULED = 'Scheduled'
    DONE = 'Done'

class ServiceOrder(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."service_order"'

    service_order_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    analysis = models.ForeignKey(ServiceAnalysis, on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class ServiceOrderItem(models.Model):
    class Meta:
        managed = False
        db_table = '"services"."service_order_item"'

    service_order_item_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    service_order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    item = models.ForeignKey('connection.ItemMasterData', on_delete=models.CASCADE) # item master data admin
    item_name = models.CharField(max_length=255, blank=True, null=True) 
    principal_item = models.ForeignKey('connection.PrincipalItem', on_delete=models.CASCADE) # mrp
    item_quantity = models.IntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)