from django import forms
from AppTwo.models import Student # or-->from first_app.models import Student


class  StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'  #fields ='var1,var2,var3' here it is all
        
        
