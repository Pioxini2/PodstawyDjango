import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from calculator.models import User

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

def get_users(request):
    users = User.objects.all()

    #return HttpResponse(f"{users}")

    users_data=[]
    for user in users:
        users_data.append(user.username)

    return JsonResponse({"users" : users_data})

'''def factorial(request):
    return HttpResponse("Tu bedzie silnia")'''