from django.forms import FileField,Form,ModelForm
from AppTwo.models import Salary


class SalaryForm(ModelForm):
    class Meta:
        model = Salary
        fields=['sname','basic','HRA','TA']
    
class UploadForm(Form):
    salary_file=FileField()
            
