from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ViewUser(LoginRequiredMixin, View):
    login_url='/login/'
    def get(self, request):
        return HttpResponse('user here')


@decorators.login_required(login_url='/login/')
def view_product(request):
    return HttpResponse('product')
