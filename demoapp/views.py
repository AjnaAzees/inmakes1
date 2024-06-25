from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import Team

# Create your views here.
def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})
def demo(request):
    object=Team.objects.all()
    return render(request,"index.html",{'results':object})
#def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#    return render(request,"result.html",{'result':res})
#   return  HttpResponse("Hello World")
#def about(request):
#    return render(request,"about.html")
#def contact(request):
#    return HttpResponse("Monday is a good day")