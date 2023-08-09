from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>Hello World</h1>")


def v1(response):
    return HttpResponse("<h1>view 1!</h1>")

def hello(request):
    return render(request,"index.html",{})