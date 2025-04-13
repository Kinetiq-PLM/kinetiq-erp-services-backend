from django.db import models  
from django.utils.timezone import now

class ItemMasterData(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."item_master_data"'

    item_id = models.CharField(primary_key=True, max_length=255,  editable=False) 
    item_type = models.TextField() 
    item_name = models.CharField(max_length=255, blank=True, null=True) 

class Policies(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."policies"'
        
    policy_id = models.CharField(primary_key=True, max_length=255,  editable=False) 
    policy_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    effective_date = models.DateField(default=now, blank=True, null=True)
    status = models.TextField() 

class Product(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."products"'

    product_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    item = models.ForeignKey(ItemMasterData, on_delete=models.SET_NULL, 
                             blank=True, null=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_level = models.IntegerField(blank=True, null=True)
    warranty_period = models.IntegerField(blank=True, null=True, default=12)
    policy = models.ForeignKey(Policies, on_delete=models.SET_NULL, 
                             blank=True, null=True)

    