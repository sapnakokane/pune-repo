from django.shortcuts import render
from app8.forms import botcls
# Create your views here.

def botview(request):
    bbb=botcls()
    if request.method=='POST':
        bbb=botcls(request.POST)
        if bbb.is_valid():
            print("validating the details & submitting...")
    return render(request,'app8/bot.html',{'bbb':bbb})

# run the program.. right click.. view source code.. u cn see bot handler & its value