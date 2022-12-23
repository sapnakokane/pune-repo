from django.shortcuts import render
from app3.models import mymodl
# Create your views here.
def modlview(request):
    mylist=mymodl.objects.all()
    return render(request,'app3/modlview.html',{'mylist':mylist})

# or
#     mylist=mymodl.objects.all()
#     mydict={'mylist':mylist}
#     return render(request,'app3/modlview.html',context=mylist)
