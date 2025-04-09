from django.db import models  

class PrincipalItem(models.Model):
    class Meta:
        managed = False
        db_table = '"mrp"."principal_items"'

    principal_item_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)  
    markup_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)  
    item = models.ForeignKey('connection.ItemMasterData', on_delete=models.CASCADE)
