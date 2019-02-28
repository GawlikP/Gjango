from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password

# Create your views here

from .forms import LoginForm
from .forms import RegisterForm
from .forms import CreatePlayerForm

from .models import User
from .models import Player

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
        form = LoginForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['name_input']):
                user = User.objects.get(username=form.cleaned_data['name_input'])
                print('user: ' + str(user.password))
                if check_password(form.cleaned_data['password_input'],user.password):
                    usr = form.cleaned_data['name_input']
                    psw = form.cleaned_data['password_input']
                    Loged_in = True
                else:
                    Error = "Password unconfirmed !"
            else:
                Error = "User Do not exist !"
        else:
            Error = "Form not valid !"
    else:
        print('no post')
        form = LoginForm()

    context = {
        'Loged_in': Loged_in,
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
    Characters = None;

    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        user = request.COOKIES['username']
        loged_in = True

    if user != None:
        Characters = Player.objects.all(user );

    if request.method == 'POST':
        print('Profile post')
        form = CreatePlayerForm(request.POST);
        if form.is_valid():
            print('Profile valid')
            try:
                user = User.objects.get(username=user);
            except:
                user = None;
            if user != None:
                name = form.cleaned_data['name_input'];
                clss = form.cleaned_data['Type_choice'];
                error = create_character(clss,name,user);

                if error:
                    print(error);
            else:
                print('Error')
    else:
        form = CreatePlayerForm()

    context = {
        'Characters': Characters,
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



# FUNCTIONS !!!!!
def create_character(clss,name,user):
    if clss == '1':
        try:
            test = Player.objects.create(name= name, user= user,
            vit= 2.0, str= 3.0, agility= 1.0, dex= 2.0, inte= 1.0,
            wis= 2.0, pow= 2.0);
            print(test + " udalo sie !")
            return "Success"
        except:
            return "Error"
        try:
            test = Player.objects.create(name= name, user=user,
            vit= 4.0, str=3.0, agility= 0.0, dex= 1.0, inte= 1.0,
            wis= 1.0, pow= 3.0);
            print(test + " udalo sie !");
        except:
            return "Error"
    elif clss == '3':
        try:
            test = Player.objects.create(name= name, user= user,
            vit= 1.0, str = 1.0, agility= 1.0, dex= 0.0, inte= 5.0,
            wis= 2.0, pow= 2.0
            );
            print(test +" udalo sie !");
        except:
            return "Error"
    elif clss == '4':
        try:
            test = Player.objects.create(name= name, user= user,
            vit = 1.0, str= 2.0, agility= 4.0, dex= 2.0, inte= 2.0,
            wis=1.0, pow=2.0);
            print(test + " udalo sie !")
        except:
            return "Error"
    elif clss == '5':
        try:
            test = Player.objects.create(name= name, user= user,
            vit=2.0, str=2.0, agility= 2.0, dex=5.0, inte= 1.0,
            wis= 1.0, pow=4.0);
            print(test + " udalo sie !!!");
        except:
            return "Error"
