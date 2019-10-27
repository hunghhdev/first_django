from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate

# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>xinchao</h1>')


class LoginClass(View):
    def get(self, request):
        return render(request, "login/login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return HttpResponse('user not found')
        return HttpResponse("ok %s %s" % (username, password))
