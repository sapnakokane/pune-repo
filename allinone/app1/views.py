from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.
def show(request):
    return HttpResponse('<h1> my response </h1>')

def student_data(request):
    obj=student.objects.all()
    my_dict={'obj':obj}
    return render(request,'app1/myhtml.html',context=my_dict)