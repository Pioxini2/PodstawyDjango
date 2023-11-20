from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    print(request)
    #View code here
    return HttpResponse(f"Hello,  World! {request.GET['x']}")

'''def factorial(request):
    return HttpResponse("Tu bedzie silnia")'''