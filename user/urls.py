from django.contrib import admin
from django.urls import path,include
from user import views

urlpatterns = [
   
    path("user_Login",views.user_Login,name='user_Login'),
    path("Register",views.Register,name='Register'),
    path("user_Logout",views.user_Logout,name='user_Logout'),
    path("index",views.index,name='index'),
]
