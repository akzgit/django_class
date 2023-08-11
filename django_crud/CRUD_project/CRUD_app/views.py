from django.shortcuts import render,redirect
from CRUD_app.forms import EmpDetails_Form
from CRUD_app.models import EmpDetails

# Create your views here.

# def index(request):
#     empobj=EmpDetails_Form()
#     return render(request,"crud_app/index.html",{'form':empobj})


def index(request):
    if request.method=='POST':
        empobj=EmpDetails_Form(request.POST)
        if empobj.is_valid():
            try:
                empobj.save()
                return redirect('/show')
            except:
                pass
    else:
        empobj=EmpDetails_Form()
        return render(request,"crud_app/index.html",{'form':empobj})    
      
def show(request):
    emp1=EmpDetails.objects.all()
    return render(request,"crud_app/show.html",{'employees':emp1})

def edit(request,id):
    emp2=EmpDetails.objects.get(id=id)
    return render(request,'crud_app/edit.html',{'emp2':emp2}) 

def update(request,id):
    emp2=EmpDetails.objects.get(id=id)      
    empobj=EmpDetails_Form(request.POST,instance=emp2)
    if empobj.is_valid():
        empobj.save()
        return redirect("/show")
    return render(request,'crud_app/edit.html',{'emp2':empobj})

def destroy(request,id):
    emp2=EmpDetails.objects.get(id=id)
    emp2.delete()
    return redirect("/show")     