from django.db import models
from service_analysis.models import ServiceAnalysis

class AnalysisStatusEnum(models.TextChoices):
    SCHEDULED = 'Scheduled'
    DONE = 'Done'

class ServiceOrder(models.Model):
    class Meta:
        db_table = '"services"."service_order"'

    service_order_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    analysis = models.ForeignKey(ServiceAnalysis, on_delete=models.CASCADE)
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

class ServiceOrderItem(models.Model):
    class Meta:
        db_table = '"services"."service_order_item"'

    service_order_item_id = models.CharField(primary_key=True, max_length=255,  editable=False)  
    service_order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    item_md = models.ForeignKey('connection.InventoryItemMD', on_delete=models.CASCADE) # inventory
    principal_item = models.ForeignKey('connection.PrincipalItem', on_delete=models.CASCADE) # mrp
    item_quantity = models.IntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def item_name(self):
        # fetches item_name from item
        return self.item_md.item.item_name if self.item_md else None