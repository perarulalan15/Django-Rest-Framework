from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def api_home(request,*args, **kwargs):
    return JsonResponse({"message": "Hi there!, this is my django api response."})