from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app3.forms import UserForm

# Create your views here.
def home_view(request):
    return render(request,'app3/home.html')

@login_required()
def python_view(request):
    return render(request,'app3/python.html')

@login_required()
def java_view(request):
    return render(request,'app3/java.html')

@login_required()
def aptitude_view(request):
    return render(request,'app3/apti.html')

def logout_view(request):
    return render(request,'app3/logout.html')

def signup_view(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'app3/signup.html',{'form':form})