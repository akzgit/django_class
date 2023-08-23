from django.db import models

class Product(models.Model):
    prod_name=models.CharField(max_length=100)
    prod_quantity=models.CharField(max_length=20)
    prod_price=models.DecimalField(max_digits=9,decimal_places=2)
    prod_desc=models.TextField()
    
    def __str__(self):
        return f"{self.prod_name}({self.prod_quantity})"
