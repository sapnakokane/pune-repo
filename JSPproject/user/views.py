from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'base/index.html')
    # types of return: render(takes u on that page) &redirect(to load the file on same path)