from django.shortcuts import render
from . forms import UploadForm
from django.views.generic.base import View
from io import TextIOwrapper
from csv import DictReader




class UploadView(View):
    def get(self,request):
        return render(request,"upload.html",{'form':UploadForm()})
    
    
    def post(self,request):
        products_file=request.FILES['product_files']
        rows=TextIOWrapper(products_file,encoding="utf-8",newline="")
        for row in DictReader(rows):
            row_count+=1
            form=ProductForm(row)
            if not form.is_valid():
                form_errors=form.errors
                break
            form.save()
        return render(request,"upload.html",{'form':UploadForm()})    
        
    
