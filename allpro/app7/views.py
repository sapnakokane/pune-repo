from django.shortcuts import render,redirect
from app7.forms import feedback,signupform
# Create your views here.
def feedbackview(request):
    fff=feedback()
    if request.method=='POST':
        fff=feedback(request.POST)
        if fff.is_valid():
            print("form validation successful")
        return redirect(signupview(request))
    return render(request,'app7/feed.html',{'fff':fff})

def signupview(request):
    sss=signupform()
    if request.method=='POST':
        sss=signupform(request.POST)
        if sss.is_valid():
            print("form validation successful")
    return render(request,'app7/signup.html',{'sss':sss})


