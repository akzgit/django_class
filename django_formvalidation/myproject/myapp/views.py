from django.shortcuts import render
from . forms import SimpleForm

def simple_form_view(request):
    if request.method=='POST':
        form=SimpleForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            age=form.cleaned_data['age']
            
    else:
        form=SimpleForm()
    return render(request,'myapp/simple_form.html',{'form':form})        

