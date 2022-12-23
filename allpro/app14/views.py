from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'app14/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request,'app14/age.html',{'name':name})
    response.set_cookie('name',name)
    return response

def gf_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    response=render(request,'app14/gf.html',{'name':name,'age':age})
    response.set_cookie('age',age)
    return response

def result_view(request):
    gf=request.GET['gf']
    age=request.COOKIES['age']
    name=request.COOKIES['name']
    response=render(request,'app14/result.html',{'name':name,'age':age,'gf':gf})
    response.set_cookie('gf',gf)  #this is temporary cookies
    return response