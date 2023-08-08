import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

#Fake data script
from faker import Faker
import random
from AppTwo.models import Employee,AccessRecord,WebPage

fakegen=Faker()
emp_name=['John','Mary','Rose','Michael','Adam']

def add_empname():
    e=Employee.objects.get_or_create(emp_name=random.choice(emp_name))[0]
    # e.save()
    return e

def populate(N=5):
    for entry in range(N):
        #trying to get the employee name for the entry
        empN=add_empname()    
        
        #create the fake data for the entry
        fake_email=fakegen.email()
        fake_desgn=fakegen.job()
        fake_date=fakegen.date()
        
        #create the new webpage entry
        webpg=WebPage.objects.get_or_create(name=empN,emp_desg=fake_desgn,emp_email=fake_email)[0]
        
        #create a fake accessrecord for the webpage
        acc_rec=AccessRecord.objects.get_or_create(email=webpg,date=fake_date)[0]


# if __name__=='main':
#     print("populating script")
#     populate(20)  
#     print("populating data completed")   

print("populating script")
populate(20)  
print("populating data completed")      
            