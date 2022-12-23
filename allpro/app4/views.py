from django.shortcuts import render,redirect
from app4.forms import myform,myform1
# Create your views here.
# def formview(request):
#     exam=myform()
#     return render(request,'app4/formview.html',{'exam':exam})

#updated as follows:

def formview(request):
    exam=myform()
    if request.method=='POST':
        exam=myform(request.POST)
        if exam.is_valid():
            print("form validation is succes & printing data:..")
            print('name: ',exam.cleaned_data['name'])
            print('age: ', exam.cleaned_data['age'])
            print('date: ',exam.cleaned_data['date'])
            print('gender: ', exam.cleaned_data['gender'])
    return render(request,'app4/formview.html',{'exam':exam})

#cleaned_data is using here to print the input data in the form on the terminal of pycharm

def formview1(request):
    exam1=myform1()
    if request.method=='POST':
        exam1=myform1(request.POST)
        if exam1.is_valid():
            print("form validation is succes & printing data:..")
            print('name: ',exam1.cleaned_data['name'])
            print('age: ', exam1.cleaned_data['age'])
            print('date: ',exam1.cleaned_data['date'])
            print('img: ', exam1.cleaned_data['img'])
            print('feedback: ', exam1.cleaned_data['feedback'])
    return render(request,'app4/feedback.html',{'exam1':exam1})

