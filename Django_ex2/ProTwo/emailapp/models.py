from django.db import models
# this model is to store the data in the admin
class Contactus(models.Model):
    from_email=models.EmailField()
    to_email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
    
    