from django.shortcuts import render

from django.http import HttpResponse

from main.models import sqdata

def index(request):
    return HttpResponse("Hello, world!")
