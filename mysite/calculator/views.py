import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def hello(request, number):
    print(request)
    #View code here
    #return HttpResponse(f"Hello,  World! {request.GET['x']}")
    return HttpResponse(f"Hello,  World! {number}")

@csrf_exempt
def calc(request):
    data = json.loads(request.body)
    if data["operation"] == "+":
        result = data["a"]+data["b"]
    return HttpResponse(f"{result}")

'''def factorial(request):
    return HttpResponse("Tu bedzie silnia")'''