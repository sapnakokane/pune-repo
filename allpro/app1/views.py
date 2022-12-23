from django.shortcuts import render
from django.http import HttpResponse
import  datetime
# Create your views here.
def morn(request):
    return HttpResponse("<h1>Hello guys good morning</h1>")

def dtym(request):
    date=datetime.datetime.now()
    return HttpResponse(str(date))

def msgtym(request):
    time=datetime.datetime.now()
    s='<h1>the current server time & date is: '+str(time)+'</h1>'
    return HttpResponse(s)

def tempmsg(request):
    tt=datetime.datetime.now()
    h=int(tt.strftime("%H"))
    msg="hello guys good "
    if h<12:
        msg=msg+"morning"
    elif h<16:
        msg=msg+"afternoon"
    elif h<21:
        msg=msg+"evening"
    else:
        msg=msg+"night"
    msg=msg+"& server time is: "+str(tt)
    return HttpResponse(msg)

def temptag(request):
    dt = datetime.datetime.now()
    return render(request,'app1/temptags.html',{'dt':dt})