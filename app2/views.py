from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat (request):
    return HttpResponse ('<marquee> <h1> DREAM HERO </marquee></h1>')

def  devilers (request):
    return HttpResponse ('<h1> I LOVE DEVILERS </h1>')
