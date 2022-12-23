from django.shortcuts import render
from app18.forms import additemForm
# Create your views here.
# session management by using session API(shopping cart application)

def additemView(request):
    add=additemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        # request.session.set_expiry(120)  -->set expiry time in seconds <--
    return render(request,'app18/additem.html',{'add':add})

def displayitemView(request):
    return render(request,'app18/displayitems.html')


#the default max_age of the session in 14 days,bt based on requirement we cn set our own expiry time

# id the session info stored inside browsers cache such type of sessions are called browser length session.

#if the session info stored persistantly inside file/database/cache, are called persistant session.

#by default sessions are persistant sessions..

