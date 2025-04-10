from django.db import models
from service_request.models import ServiceRequest

class Customer(models.Model):
    class Meta:
        managed = False
        db_table = '"sales"."customers"'

    customer_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)  
    phone_number = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)

class Statement(models.Model):
    class Meta:
        managed = False
        db_table = '"sales"."statement"'

    statement_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    customer = models.ForeignKey('connection.Customer', on_delete=models.CASCADE)
    salesrep = models.ForeignKey('connection.Employee', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    type = models.TextField() 
    total_tax = models.IntegerField(default=0)

class Order(models.Model):
    class Meta:
        managed = False
        db_table = '"sales"."orders"'

    order_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.TextField() 
    order_total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 
    order_type = models.TextField() 

class StatementItem(models.Model):
    class Meta:
        managed = False
        db_table = '"sales"."statement_item"'

    statement_item_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    product = models.ForeignKey("connection.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    additional_service = models.ForeignKey('connection.AddsService', on_delete=models.CASCADE)