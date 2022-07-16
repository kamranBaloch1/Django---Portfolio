

from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from .models import Project, Blog, Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.


def index(request):
    project = Project.objects.all()[0:3]
    proDic = {"projects": project}
    return render(request, "index.html", proDic)


def project(request, slug):

    fltr = Project.objects.filter(slug=slug).first
    dic = {"myproject": fltr}
    return render(request, "projectView.html", dic)


def allprojects(request):
    allprojectts = Project.objects.all().order_by('-release_date')
    allprojectsDic = {"allprojects": allprojectts}
    return render(request, "allprojects.html", allprojectsDic)


def blogs(request):
    allblogs = Blog.objects.all().order_by('-release_date')
    allblogDic = {"blogs": allblogs}
    return render(request, "blogs.html", allblogDic)


def blogpost(request, slug):
    singleBlog = Blog.objects.filter(slug=slug).first
    singleBlogDic = {"singleBlog": singleBlog}
    return render(request, "blogpost.html", singleBlogDic)


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact.objects.create(
            name=full_name, email=email, message=message)
        messages.warning(request, 'Thanks ' + full_name + " for contacting us")
    return render(request, "contact.html")



def loginUser(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        userLogin = authenticate(username=username, password=password)
        if userLogin is not None:
            login(request, userLogin)
            messages.success(request, "Welcome " + username)
            return redirect('/')
        else:
            messages.warning(request, "Please check your username or password")
            return redirect('login')

    return render(request, "login.html")


def signup(request):

    if request.method == "POST":

        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        Cpassword = request.POST['Cpassword']

        if(password == Cpassword):

            if User.objects.filter(username=username).first():
                messages.warning(request, "This username is already taken")

            else:
                useer = User.objects.create_user(
                    username=username, email=email, password=password)
                useer.save()
                messages.success(
                    request, " Your account has been successfully created")
                return redirect("/")
        else:
            messages.warning(
                request, "Password and confirm password did'nt matched")

    return render(request, "signup.html")

def logoutUser(request):

    logout(request)
    messages.success(request,"You have been loggedOut")
    return redirect("/")
    return HttpResponse("You have been loggedOut")
    