# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from wodo.models import workers, workRating, filterCache, appUser
import json
import math
import statistics
from geopy.distance import geodesic

def checkUser(request):
    types = request.headers.get("type")
    token = request.headers.get("token")


    if types == "phone":
        user = appUser.objects.filter(contact=token)
        if len(user)!=0:
            response = {
                "status" : "success",
                "user" : "old",
                "token" : user[0].username
            }
        else:
            response = {
                "status" : "success",
                "user" : "new",
                "token" : ""
            }
    else:
        user = appUser.objects.filter(username=token)
        if len(user)!=0:
            response = {
                "status" : "success",
                "user" : "old",
                "token" : user[0].username
            }
        else:
            response = {
                "status" : "success",
                "user" : "new",
                "token" : "" 
            }
    return JsonResponse(response, safe=False, status=200)

def createUser(request):
    token = request.headers.get("token")
    name = request.headers.get("name")
    email = request.headers.get("email")
    profile = request.headers.get("profile")
    contact = request.headers.get("contact")

    user = appUser(username=token, name=name, contact=contact, profile=profile, email=email)
    user.save()

    response = {
        "status" : "success",
        "token" : token,
        "message" : "User added successfully"
    }

    return JsonResponse(response, safe=False, status=200)