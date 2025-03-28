from django.db import models  

class OpCost(models.Model):
    class Meta:
        managed = False
        db_table = '"distribution"."operational_cost"'

    operational_cost_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    total_operational_cost = models.DecimalField(max_digits=10, decimal_places=2)
