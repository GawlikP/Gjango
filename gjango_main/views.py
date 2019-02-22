from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password

# Create your views here

from .forms import LoginForm
from .forms import RegisterForm

from .models import User

def index(request):

    context = {
        'title':'Gjango',
        'navi_one':'active'
    }

    return render(request,'main.html',context)
def profile(request):

    context = {
        'title':'Profile',
        'navi_two':'active',
    }

    return render(request,'main.html',context)

def registration(request):

    form = None

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            usrnm = form.cleaned_data['name_input']
            password = form.cleaned_data['password_input']
    else:
        form = RegisterForm()

    context = {
        'form':form,
        'navi_four':'active',
        'title':'Registration'
    }

    return render(request,'register.html',context)

def login(request):

    form = None
    Registered = False
    Error = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.cleaned_data['name_input']):
                usr = form.cleaned_data['name_input']
                psw = form.cleaned_data['password_input']
                user = User.objects.create(username=usr,password = make_password(psw))
                Registered = True
            else:
                Error = "User Already exist !"
        else:
            Error = "Form not valid !"
    else:
        form = LoginForm()

    context = {
        'form':form,
        'title':'Loging in',
        'registered':Registered,
        'Error': Error
    }

    return render(request,'loging_in.html',context)
