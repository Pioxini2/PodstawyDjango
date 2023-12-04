import hashlib
import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from calculator.models import Note, User

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
        users_data.append((user.username, user.password))

    return JsonResponse({"users" : users_data})

@csrf_exempt
def add_user(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    users=User.objects.all()
    for existing_user in users:
        if existing_user.username == username:
            return HttpResponse("Users already exists!", status=400)

    user = User(username=username, password=password)
    user.save()

    return JsonResponse({"username": user.username, "password": user.password})

@csrf_exempt
def login(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    try:
        user = User.objects.get(username=username, password=password)
        user.login_count += 1
        user.save()
        return HttpResponse("User does exists!", status=200)
    except:
        return HttpResponse("User does not exists!", status=404)


@csrf_exempt
def get_notes(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    min_length = data.get("min_length", 0)
    password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    try:
        user = User.objects.get(username=username, password=password)
    except:
        return HttpResponse("User does not exists!", status=404)

    notes = Note.objects.filter(user=user)

    notes_data=[]
    for note in notes:
        if note.is_longer_than(min_length):
            notes_data.append((note.content))

    return JsonResponse({"notes" : notes_data})

'''def factorial(request):
    return HttpResponse("Tu bedzie silnia")'''