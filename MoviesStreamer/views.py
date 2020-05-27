from django.shortcuts import render
from django.http import HttpResponse



dummyData  = [
    {
        'MovieName':'Deadpool',
        'Relase Date' : "Today"  
    },
        {
        'MovieName':'Thor',
        'Relase Date' : "13 May,2000"  
    }
] 


def home(request):
    context = {
        'Movies'  : dummyData
    }
    return render(request,'MoviesStreamer/home.html',context)
    # return HttpResponse("<h1> Home <H1>")

def about(request):
    # return HttpResponse("<h1> About <H1>")
    return render(request,'MoviesStreamer/about.html',{'title': "My App Aboutpage"})



# Create your views here.
