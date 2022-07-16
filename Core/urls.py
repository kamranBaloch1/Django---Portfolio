
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("project/<str:slug>",views.project,name="project"),
    path("allprojects/",views.allprojects,name="allprojects"),
    path("blogs/",views.blogs,name="blogs"),
    path("blogpost/<str:slug>",views.blogpost,name="blogpost"),
    path("contact/",views.contact,name="contact"),
    path("login/",views.loginUser,name="loginUser"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logoutUser,name="logout"),
   
]
