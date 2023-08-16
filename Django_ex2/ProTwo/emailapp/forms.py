from django import forms
class Contactus(forms.Form):
    from_email=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message=forms.CharField(required=True,widget=forms.Textarea)
    
    