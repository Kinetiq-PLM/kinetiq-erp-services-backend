from django.db import models  

class Department(models.Model):
    class Meta:
        managed = False
        db_table = '"human_resources"."departments"'

    dept_id = models.CharField(primary_key=True, max_length=255, editable=False) 
    dept_name = models.CharField(max_length=100, unique=True)

class Employee(models.Model):
    class Meta:
        managed = False
        db_table = '"human_resources"."employees"'
    
    employee_id = models.CharField(primary_key=True, max_length=255, editable=False)  
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL,
                             blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)  
    phone = models.CharField(max_length=20, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    status = models.TextField() 
    updated_at = models.DateTimeField(auto_now_add=True)