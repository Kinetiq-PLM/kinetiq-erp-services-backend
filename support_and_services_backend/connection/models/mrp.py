from django.db import models  
from service_order.models import ServiceOrderItem

class PrincipalItem(models.Model):
    class Meta:
        managed = False
        db_table = '"mrp"."principal_items"'

    principal_item_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    service_order_item = models.ForeignKey(ServiceOrderItem, on_delete=models.CASCADE, null=False, blank=True) 
    mark_up_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)  
    item = models.ForeignKey('connection.ItemMasterData', on_delete=models.CASCADE)
