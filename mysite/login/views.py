from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
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


class AddPost(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        f = PostForm()
        context = {'fm': f}
        return render(request, 'login/add_post.html', context)
    
    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('fail data')
        print(request.user.get_all_permissions())
        if request.user.has_perm('login.add_post'):
            f.save()
        else:
            return HttpResponse('not perm')
        return HttpResponse('ok')