from django import forms
from AppTwo.models import Student # or-->from first_app.models import Student
from django.core import validators


# class  StudentForm(forms.ModelForm):
#     class Meta:
#         model=Student
#         fields='__all__'  #fields ='var1,var2,var3' here it is all


#user-defined validation
def check(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError("Name need to be started with A")
    

class StudentForm(forms.Form) :
      student_name =forms.CharField(validators =[check],max_length=50)
      student_course = forms.CharField(max_length=50)    
        
        
