from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("hello galaxy")


def xyz(request):
    return HttpResponse("<h1>hello galaxy</h1>")
