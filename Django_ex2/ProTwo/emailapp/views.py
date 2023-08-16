from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from . forms import Contactus
# Create your views here.

def contactview(request):
    if request.method =="GET":
        formobj=Contactus()
        
    else:
        formobj=Contactus(request.POST)
        if formobj.is_valid():
            subject=formobj.cleaned_data["subject"]
            from_email=formobj.cleaned_data["from_email"]
            message=formobj.cleaned_data["message"]
            try:
                send_mail(subject,message,from_email,['admin@test.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect("success")
    return render(request,"emailapp/email.html",{"form":formobj})  


def successview(request):
    return HttpResponse("Success. Thankyou for your message")         