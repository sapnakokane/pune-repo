from django.shortcuts import render
from app15.forms import additemForm
# Create your views here.

def index(request):
    return render(request,'app15/home.html')
def additem(request):
    cart=additemForm()
    response=render(request,'app15/additem.html',{'cart':cart})
    if request.method=='POST':
        cart=additemForm(request.POST)
        if cart.is_valid():
            name=cart.cleaned_data['name']
            quantity=cart.cleaned_data['quantity']
            response.set_cookie(name,quantity,180)
            # return index(request)
    return response
def displayitem(request):
    return render(request,'app15/showitem.html')