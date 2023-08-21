from django import forms
from . models import Contactus
from django.forms import ModelForm
class Contactus_forms(ModelForm):
    # from_email=forms.EmailField(required=True)
    # to_email=forms.EmailField(required=True)
    # subject=forms.CharField(required=True)
    # message=forms.CharField(required=True,widget=forms.Textarea)
    cobj = Contactus()
    class Meta:
        model=Contactus
        fields='__all__'
    