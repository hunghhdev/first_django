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


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail_question.html', {'qs': q})


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST['choice']
        c = q.choice_set.get(pk=data)
        c.vote = c.vote + 1
        c.save()
    except:
        HttpResponse('not found choice')
    return render(request, 'polls/result.html', {'q': q})
