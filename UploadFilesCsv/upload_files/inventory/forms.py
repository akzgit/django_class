from django.forms import FileField,Form,ModelForm
from . models import Product

class ProductForm(ModelForm):
    class Meta:
        model =Product
        ProductFields=["prod_name","prod_quantity","prod_price","prod_desc"]


class UploadForm(Form):
    product_file=FileField()        