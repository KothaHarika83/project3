from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def teja(request):
    return render(request,'teja.html')
def efg(request):
    return HttpResponse('teja')