from django.shortcuts import render
from .forms import MoviesForm
# Create your views here.
def Moviesview(request):
    mmm=MoviesForm()
    if request.method=='POST':
        mmm=MoviesForm(request.POST)
        if mmm.is_valid():
            mmm.save()
    return render(request,'app10/datewidget.html',{'mmm':mmm})