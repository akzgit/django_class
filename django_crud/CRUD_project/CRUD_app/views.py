from django.shortcuts import render,redirect,HttpResponse
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

 #checking cookies on browser   
def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("checking cookies on browser")
    
def cookie_delete(request):
    if request.session.test_cookie_worked(): #if it returns true
        request.session.delete_test_cookie() #it will delete the cookie
        response=HttpResponse("cookie deleted successfully")
    else:
        response=HttpResponse("Your browser doesn't accept cookies")  
    return response 


#sessions
def create_session(request):
    request.session['name']='username'
    request.session['password']='password123'
    return HttpResponse("Session is set")

def access_session(request):
    if request.session.get('name','Akash'):
        response="Name :{0}".format(request.session.get('name'))
    if request.session.get('password','Akash123'):
        response+="Password :{0}".format(request.session.get('password'))
    #     return HttpResponse(response)
    # else:
    #     return redirect('createsession/') 
    
    if not response:
        return HttpResponse("No session records found")
    else:
        return HttpResponse(response)
    

def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("session data deleted")
                     