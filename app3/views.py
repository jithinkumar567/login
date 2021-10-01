from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1fun(request):
    return HttpResponse('How are you')
def loginfun(request):
    return render(request,'login.html')
