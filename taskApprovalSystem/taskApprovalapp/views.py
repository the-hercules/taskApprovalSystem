# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello you are in the app")
# Create your views here.
