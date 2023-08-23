from django.shortcuts import render,redirect
from django.http import HttpResponse
from AppTwo.models import Employee,AccessRecord,WebPage
from salary import UploadForm
from django.views.generic.base import View
from AppTwo.form import StudentForm

def index(request):
    return HttpResponse("<em>My Second App</em>")


def help(request):
    return render(request,'help.html')

def empdetails(request):
    # webpage_list=AccessRecord.objects.order_by('date')
    # date_dict={'acces_records':webpage_list}
    WebPage_list=WebPage.objects.order_by('emp_desg')
    desg_dict={'access_webpage':WebPage_list}
    return render(request,'AppTwo/empdetails.html',context=desg_dict)

class UploadView(View):
    
    def get(self,request):
        return render(request,"AppTwo/upload.html",{"form":UploadForm()})

def student_views(request):
    studobj=StudentForm()
    return render(request,"AppTwo/form.html",{'form':studobj})
 
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
    request.session['name']='usename'
    request.session['password']='password123'
    return HttpResponse("Session is set")

def access_session(request):
    response=""
    if request.session.get('name','Akash'):
        response="Name :{0}".format(request.session.get('name'))
    if request.session.get('password','Akash123'):
        response+="Password :{0}".format(request.session.get('password'))
        return response
    else:
        return redirect('createsession/')                    