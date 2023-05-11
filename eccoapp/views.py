from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')

def dashboard(request):
    return render(request, 'Dashboard/dashboard.html')


def allusers(request):
    return render(request, 'Dashboard/alluser.html')


def addnewuser(request):
    return render(request, 'Dashboard/addnewuser.html')

def login(request):
    return render(request, 'Dashboard/login.html')


def register(request):
    return render(request, 'Dashboard/register.html')


def forgotpassword(request):
    return render(request, 'Dashboard/forgotpassword.html')

def emailverification(request):
    return render(request, 'Dashboard/emailverification.html')

def settings(request):
    return render(request, 'Dashboard/settings.html')
   