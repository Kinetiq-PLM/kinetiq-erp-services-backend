from django.db import models  

class InventoryItemMD(models.Model):
    class Meta:
        managed = False
        db_table = '"inventory"."inventory_item"'

    inventory_item_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    item_type = models.TextField(blank=True, null=True)
    item = models.ForeignKey('connection.ItemMasterData', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('connection.Warehouse', on_delete=models.CASCADE)
    current_quantity = models.IntegerField(null=False)
