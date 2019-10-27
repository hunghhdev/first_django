from django.urls import path
from . import views


app_name = 'login'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login')
]
