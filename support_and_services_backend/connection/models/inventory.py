from django.db import models  

class ProductDocumentItem(models.Model):
    class Meta:
        managed = False
        db_table = '"operations"."product_document_items"'

    productdocu_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    product = models.ForeignKey('connection.Product', on_delete=models.CASCADE)

class InventoryItemMD(models.Model):
    class Meta:
        managed = False
        db_table = '"inventory"."inventory_item"'

    inventory_item_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    item_type = models.TextField(blank=True, null=True)
    productdocu = models.ForeignKey(ProductDocumentItem, on_delete=models.CASCADE)
    material = models.ForeignKey('connection.RawMaterial', on_delete=models.CASCADE)
    current_quantity = models.IntegerField(null=False)
