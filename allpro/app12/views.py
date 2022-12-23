from django.shortcuts import render
from app12.models import tempfil
# Create your views here.

def tempfilview(request):
    modl=tempfil.objects.all()
    return render(request,'app12/advfilter.html',{'modl':modl})