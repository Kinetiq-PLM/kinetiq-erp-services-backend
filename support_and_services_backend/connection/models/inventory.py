from django.db import models  

class InventoryItemMD(models.Model):
    class Meta:
        managed = False
        db_table = '"inventory"."inventory_item_master_data"'

    item_md_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    item = models.ForeignKey('connection.ItemMasterData', on_delete=models.CASCADE)
    available_stock = models.IntegerField(null=False)
