from django.shortcuts import render
from app17.forms import NameForm,AgeForm,GFForm
# Create your views here.
# Session management by using session API(profile creation)

def naview(request):
    ppp=NameForm()
    return render(request,'app17/name.html',{'ppp':ppp})
def agview(request):
    name=request.GET['name']
    request.session['name']=name
    ppp=AgeForm()
    return render(request,'app17/age.html',{'ppp':ppp})

def gfview(request):
    age=request.GET['age']
    request.session['age']=age
    ppp=GFForm()
    return render(request,'app17/gf.html',{'ppp':ppp})

def resultvieww(request):
    gf=request.GET['gf']
    request.session['gf']=gf
    return render(request,'app17/result.html')


