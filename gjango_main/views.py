from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password

# Create your views here

from .forms import LoginForm
from .forms import RegisterForm
from .forms import CreatePlayerForm

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
        'is_logged': Loged_in,
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

def profile(request):

    user = None
    loged_in = False
    form = None

    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        user = request.COOKIES['username']
        loged_in = True


    if request.method == 'POST':
        form = CreatePlayerForm(request.POST);
    else:
        form = CreatePlayerForm()

    context = {
        'form': form,
        'username': user,
        'is_logged': loged_in,
        'navi_two':'active',
        'title': 'Profile'

    }


    return render(request, 'profile.html',context)

def logout(request):
    user = None
    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        user = request.COOKIES['username']

    context = {
        'title': 'Loging_out'
    }

    response = render(request,'logout.html',context)
    try :
        response.delete_cookie('username')
        response.delete_cookie('password')
    except:
        print('error')
    return response

def game(request):

    user = None
    loged_in = False
    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        user = request.COOKIES['username']
        loged_in = True



    context = {
        'navi_three': 'active',
        'is_logged': loged_in,
        'title': 'Game'
    }

    response = render(request,'game.html',context);

    return response;
