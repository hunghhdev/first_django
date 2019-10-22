from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.


def index(request):  # function based views
    myname = "who am i"
    xyz = ["phone", "laptop", "aircraft"]
    context = {"name": myname, "item": xyz}
    return render(request, "polls/index.html", context)


def viewlist(request):
    list_question = Question.objects.all()
    context = {'questions': list_question}
    return render(request, 'polls/questions.html', context)
