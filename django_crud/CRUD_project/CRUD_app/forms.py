from django import forms
from CRUD_app.models import EmpDetails

class EmpDetails_Form(forms.ModelForm):
    class Meta:
        model=EmpDetails
        fields='__all__'