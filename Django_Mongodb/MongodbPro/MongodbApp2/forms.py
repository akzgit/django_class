from django import forms

class BookForm(forms.Form):
    book_name = forms.CharField(max_length=100)
    book_type = forms.CharField(max_length=100)
    book_price = forms.DecimalField()