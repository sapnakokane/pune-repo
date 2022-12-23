from django.shortcuts import render,redirect
from app9.forms import smodlForm
from app9.models import smodl

# Create your views here.
def smodlView(request):
    fff=smodlForm()
    if request.method=='POST':
        fff=smodlForm(request.POST)
        if fff.is_valid():
            fff.save()
    return render(request,'app9/modlform.html',{'fff':fff})

def smodlshow(request):
    malist=smodl.objects.all()
    return render(request,'app9/viewtable.html',{'malist':malist})


