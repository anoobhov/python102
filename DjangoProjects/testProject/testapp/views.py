from .models import User, Todo

from django.shortcuts import render

from django.http import HttpResponse , JsonResponse

from .serializers import Userserializer,Todoserializer
import json


# Create your views here.

def hello_world(request):
    return HttpResponse("Hello u built an API")

def add(request):
    a = int(request.GET.get("a"))
    b = int(request.GET.get("b"))
    c = a+b
    response = {
        "message":"success",
        "sum is : ": c
    }
    return JsonResponse(response,status=201)

def create_user(request):
    try:
        data = json.loads(request.body)

        serializer = Userserializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return JsonResponse(Userserializer(user).data)
    except Exception as e:
        return JsonResponse({
            "error":e.__str__()
        },status=400)

def get_user(request):
    try:
        user_id = int(request.GET.get("id"))
        user = User.objects.get(pk=user_id)

        return JsonResponse(Userserializer(user).data,status=200)
    except Exception as e:
        return JsonResponse({
            "message":e.__str__()
        },status=404)


def add_todo(request):
    try:
        data=json.loads(request.body)
        serializer = Todoserializer(data=data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return JsonResponse(Todoserializer(todo).data,status=201)
    except Exception as e:
        return JsonResponse({
            "message":e.__str__()
        },status=400)

def get_todo(request):
    try:
        todo_id=int(request.Get.get("id"))
        todo=Todo.objects.get(pk=todo_id)
        return JsonResponse(Todoserializer(todo).data,status=200)
    except Exception as e:
        return JsonResponse({
            "message":e.__str__()
        },status=404)