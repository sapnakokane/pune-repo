from django.shortcuts import render
from app5.forms import formex
# Create your views here.

def formexview(request):
    myform=formex()
    if request.method=='POST':
        myform=formex(request.POST)
        if myform.is_valid():
            print("form is submitted")
            print('name: ',myform.cleaned_data['name'])
            print('rollno: ',myform.cleaned_data['rollno'])
            print('email: ', myform.cleaned_data['email'])
            print('feedback: ', myform.cleaned_data['feedback'])
    return render(request,'app5/validation.html',{'myform':myform})

