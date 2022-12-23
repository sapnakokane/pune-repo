from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app2/home.html')
def movies(request):
    return render(request,'app2/movies.html')
def sports(request):
    mydict={
        'msg1':'circket is the favorite sport of all boys',
        'msg2': 'hockey is the national sport of india',
        'msg3': 'football is one of the best outdoor game',
    }
    return render(request, 'app2/sports.html',context=mydict)