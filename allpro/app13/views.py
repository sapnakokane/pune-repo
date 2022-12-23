import datetime

from django.shortcuts import render
from django.http import HttpResponse
from app13.forms import cform
# Create your views here.

def index_view(request):
    request.session.set_test_cookie()
    if request.session.test_cookie_worked():
        print("cookies are working properly..")
        request.session.delete_test_cookie()
    return HttpResponse("<h1> checking response </h1>")

#session management by using cookies:Page count application
def count_view(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'app13/count.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response

# session management by using cookies(datetime&loginform)
def cformview(request):
    fff=cform()
    return render(request,'app13/home.html',{'fff':fff})

def date_time_view(request):
    # fff=cform(request.GET)
    name= request.GET['name']
    response=render(request,'app13/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response

def result_view(request):
    name=request.COOKIES['name']
    date_time=datetime.datetime.now()
    return render(request,'app13/result.html',{'name':name,'date_time':date_time})