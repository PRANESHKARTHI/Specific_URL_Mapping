from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def abd(request):
    return render(request,"abd.html")

def steyn(request):
    return HttpResponse("Best Pacer")