from django.urls import path
from . import views


app_name = 'login'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('user-view/', views.ViewUser.as_view(), name='user_view'),
    path('view-product/', views.view_product, name='view-product')
]
