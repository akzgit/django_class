from django.shortcuts import render
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
    return render(request,"AppTwo/form.html",{'formdict':studobj})
    