from django.shortcuts import render,redirect
from app4.models import SapModel
from app4.forms import SapForm
#Create your views here.

def retrive_view(request):
    read=SapModel.objects.all()
    return render(request,'app4/index.html',{'read':read})

def create_view(request):
    form=SapForm()
    if request.method=='POST':
        form=SapForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'app4/create.html',{'form':form})

def delete_view(request,id):
    sappu=SapModel.objects.get(id=id)
    sappu.delete()
    return redirect('/')

def update_view(request,id):
    sappu=SapModel.objects.get(id=id)
    if request.method=='POST':
        form=SapForm(request.POST,instance=sappu)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'app4/update.html',{'sappu':sappu})







