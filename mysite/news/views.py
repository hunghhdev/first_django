from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from  django.views import View

# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse('xin chao')


class ClassSaveNews(View):
    def get(self, request):
        f = PostForm()
        return render(request, 'news/add_news.html', {'f': f})

    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('valid false')


def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})


def process(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            title = m.cleaned_data['title']
            content = m.cleaned_data['content']
            cc = m.cleaned_data['cc']
            email = m.cleaned_data['email']
            context = {'title': title, 'cc': cc, 'content': content, 'email': email}

            context_new = {'email_data': m}
            return render(request, 'news/print_email.html', context_new)
        else:
            return HttpResponse('valid false')
    else:
        return HttpResponse('not post method')
