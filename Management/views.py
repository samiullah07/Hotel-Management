from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse

# Create your views here.

def Index(request):
    return HttpResponse("Hello")