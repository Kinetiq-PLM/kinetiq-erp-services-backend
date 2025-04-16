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
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_level = models.IntegerField(blank=True, null=True)
    warranty_period = models.IntegerField(blank=True, null=True, default=12)
    policy = models.ForeignKey(Policies, on_delete=models.SET_NULL, blank=True, null=True)

class RawMaterial(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."raw_materials"'

    material_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    material_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class RolesPermission(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."roles_permission"'

    role_id = models.CharField(primary_key=True, max_length=255)
    role_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    permissions = models.TextField(blank=True, null=True)
    access_level = models.TextField(blank=True, null=True)  

class Users(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."users"'

    user_id = models.CharField(primary_key=True, max_length=255)
    employee_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(RolesPermission, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  
    type = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    