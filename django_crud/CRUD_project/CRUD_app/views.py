from django.shortcuts import render
from CRUD_app.forms import EmpDetails_Form

# Create your views here.

def index(request):
    empobj=EmpDetails_Form()
    return render(request,"crud_app/index.html",{'form':empobj})