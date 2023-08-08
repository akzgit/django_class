from django.contrib import admin
from AppTwo.models import Employee,WebPage,AccessRecord,Salary

admin.site.register(AccessRecord)
admin.site.register(Employee)
admin.site.register(WebPage)
admin.site.register(Salary)


#python manage.py migrate
#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver