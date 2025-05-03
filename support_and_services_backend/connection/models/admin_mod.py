from django.db import models  
from django.utils.timezone import now

class Warehouse(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."warehouse"'

    warehouse_id = models.CharField(primary_key=True, max_length=255,  editable=False) 
    warehouse_location = models.CharField(max_length=255, blank=True, null=True) 
    warehouse_name = models.CharField(max_length=50, blank=True, null=True) 

class ItemMasterData(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."item_master_data"'

    item_id = models.CharField(primary_key=True, max_length=255,  editable=False) 
    item_type = models.TextField() 
    item_name = models.CharField(max_length=255, blank=True, null=True) 

class RolesPermission(models.Model):
    class Meta:
        managed = False
        db_table = '"admin"."roles_permission"'

    role_id = models.CharField(primary_key=True, max_length=255)

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

    