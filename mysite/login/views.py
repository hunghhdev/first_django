from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login

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
            return HttpResponse('login fail')

        login(request, my_user)
        return render(request, 'login/sucess.html')


class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('login please')
        else:
            return HttpResponse('user here')
