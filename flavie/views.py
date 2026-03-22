from django.http import HttpResponse 
from django.shortcuts import render

#creation des vues

def base(request):
    return render(request,'base.html')