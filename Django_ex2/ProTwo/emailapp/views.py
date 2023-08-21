from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from . forms import Contactus
from django.conf import settings
# Create your views here.

def contactview(request):
    if request.method =="GET":
        formobj=Contactus()
        
    else:
        formobj=Contactus(request.POST)
        if formobj.is_valid():
            subject=formobj.cleaned_data["subject"]
            from_email=formobj.cleaned_data["from_email"]
            to_email=formobj.cleaned_data["to_email"]
            message=formobj.cleaned_data["message"]
            try:
                # send_mail(subject,message,from_email,['admin@test.com']) #->to display the email in the terminal
                # send_mail(subject,message, settings.EMAIL_HOST_USER,[settings.RECIPIENT_ADDRESS]) #=>email is directly given in the env
                send_mail(subject,message, settings.EMAIL_HOST_USER,[to_email])   # here email is given in the form
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect("success")
    return render(request,"emailapp/email.html",{"form":formobj})  


def successview(request):
    return HttpResponse("Success. Thankyou for your message")         