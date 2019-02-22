from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password

# Create your views here

from .forms import LoginForm
from .forms import RegisterForm

from .models import User

def index(request):

    users = None
    Loged_in = False
    if 'username' in  request.COOKIES and 'password' in request.COOKIES:
        Loged_in = True

    users = User.objects.all()[:10]



    context = {
        'is_logged':Loged_in,
        'users':users,
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
    Registered = False

    Error = None

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('valid')
            if not User.objects.filter(username=form.cleaned_data['name_input']):
                usr = form.cleaned_data['name_input']
                psw = form.cleaned_data['password_input']
                user = User.objects.create(username=usr,password = make_password(psw))
                Registered = True
                print('created')
            else:
                Error = "User Already exist !"
        else:
            Error = "Not valid form"
    else:
        form = RegisterForm()

    context = {
        'Registered':Registered,
        'form':form,
        'Error':Error,
        'navi_four':'active',
        'title':'Registration'
    }

    return render(request,'register.html',context)

def login(request):

    #form = None
    Registered = False
    Error = None
    Loged_in = False
    usr = ""
    psw = ""

    if request.method == 'POST':
        print('post')
        form = LoginForm(request.POST)
        if form.is_valid():
            print('valid')
            if User.objects.filter(username=form.cleaned_data['name_input']):
                usr = form.cleaned_data['name_input']
                psw = form.cleaned_data['password_input']
                Loged_in = True
            else:
                Error = "User Do not exist !"
        else:
            Error = "Form not valid !"
    else:
        print('no post')
        form = LoginForm()

    context = {
        'form':form,
        'title':'Loging in',
        'Error': Error
    }
    response = render(request,'loging_in.html', context)

    if Loged_in:
        print('setting cookies')
        response.set_cookie('username',usr),
        response.set_cookie('password',psw),

    return response
