from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'app2/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request,'app2/age.html')
    response.set_cookie('name',name)
    return response

def gf_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    response=render(request,'app2/gf.html',{'name':name})
    response.set_cookie('age',age)
    return response

def result_view(request):
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    gfnam=request.GET['gfnam']
    response=render(request,'app2/results.html',{'name':name,'age':age,'gfnam':gfnam})
    return response

