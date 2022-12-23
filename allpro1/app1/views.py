from django.shortcuts import render

# Create your views here.

def count_view(request):
    count=int(request.COOKIES.get('count',0))
    newcnt=count+1
    response=render(request,'app1/count.html',{'count':newcnt})
    response.set_cookie('count',newcnt)
    return response

