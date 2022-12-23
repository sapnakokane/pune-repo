from django.shortcuts import render

# Create your views here.
def blockview(request):
    return render(request,'app11/child.html')

