from django.db import models

class Employee(models.Model):
    emp_name=models.CharField(max_length=264,unique=True)  #CharField to store characters(text)
    
    def __str__(self):
        return self.emp_name
    
class WebPage(models.Model):
    name=models.ForeignKey(Employee, on_delete=models.CASCADE) 
    emp_desg=models.CharField(max_length=264)
    emp_email=models.EmailField(unique=True) 
    
    def __str__(self):
        return self.emp_desg


class AccessRecord(models.Model):
    email=models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date=models.DateField()
    
    def __str__(self):
        return self.date     
    
    
class Salary(models.Model):
    sname=models.ForeignKey(Employee,on_delete=models.CASCADE)
    basic=models.DecimalField(max_digits=9, decimal_places=2)
    HRA=models.DecimalField(max_digits=9,decimal_places=2)
    TA=models.DecimalField(max_digits=9,decimal_places=2)
    
    def __str__(self):
        return f"{self.sname({self.basic})}"