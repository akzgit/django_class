from django.db import models

# Create your models here.
class EmpDetails(models.Model):
    empid=models.CharField(max_length=20)
    empname=models.CharField(max_length=50)
    empemail=models.EmailField()
    empcontact=models.BigIntegerField()
    
    class Meta:
        db_table='EmpDetails'