from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.

def home(request):
    return HttpResponse("This is my home page")