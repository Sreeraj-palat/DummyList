import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homefun(request):
    return render(request,'home.html')

def studentfun(request):
    return render(request,'student.html') 

def viewstudentfun(request):
    return render(request,'viewstudent.html')

def galaryfun(request):
    return render(request,'galary.html')            
