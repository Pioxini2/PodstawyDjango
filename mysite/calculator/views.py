from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def hello(request, number):
    print(request)
    #View code here
    #return HttpResponse(f"Hello,  World! {request.GET['x']}")
    return HttpResponse(f"Hello,  World! {number}")

def calc(request):
    pass
    return HttpResponse("")

'''def factorial(request):
    return HttpResponse("Tu bedzie silnia")'''