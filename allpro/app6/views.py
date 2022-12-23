from django.shortcuts import render
from app6.forms import reform
# Create your views here.
def reformview(request):
    fff=reform()
    if request.method=="POST":
        fff=reform(request.POST)
        if fff.is_valid():
            print("validating details...")
    return render(request,'app6/impvalidators.html',{'fff':fff})