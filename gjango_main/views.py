from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password

# Create your views here

from .forms import LoginForm
from .forms import RegisterForm
from .forms import CreatePlayerForm

from .models import User
from .models import Player

from gjango_main.char_cre import *

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
        try:
            print('Trying to find user')
            ussr = User.objects.get(username= user);
        except:
            print('User not found')
            ussr = None;

        if ussr != None:
            print('Getting Characters')
            Characters = Player.objects.all().filter(user=ussr);


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
                error = None
                if Player.objects.filter(name= name).count() == 0:
                    error = create_character(clss,name,user);
                else:
                    print('already exits')
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

def character(response,id):
    try:
        character = Player.objects.get(id= id);
    except:
        return HttpResponse('Error 404 XD');

    loged_in = False

    if 'username' in response.COOKIES and 'password' in response.COOKIES:
        user = response.COOKIES['username'];
        loged_in = True


    context = {
    'title': 'Character',
    'is_logged': loged_in,
    'character': character
    }

    return render(response, 'character.html', context);


# FUNCTIONS !!!!!

def create_character(clss,name,user):
    if clss == '1':
        c = set_random_perks(Warrior);
        stats = get_stats_from_perks(c)

        #try:
        test = Player.objects.create(name= name, user= user, clss='Warrrior',
        vit= c[0], str= c[1], agility= c[2],dex= c[3], inte= c[4], wis=c[5],
        pow= c[6], defen= c[7],hp= stats[0],
        max_hp= stats[0], mp= stats[1], max_mp= stats[1],speed= stats[2],
        dmg= stats[3], armor= stats[4], crit_chance= stats[5], armmor_pen= stats[6],
        regeneration= stats[7], mana_regeneration= stats[8], s_pow= stats[9],
        magic_pen= stats[10], magic_a= stats[11], dodge= stats[12]);
        #print(test + " udalo sie !")
        return "Success"
        #except:
        #    return "Error"
    elif clss == '2':
        c = set_random_perks(Barbarian);
        stats = get_stats_from_perks(c)

        #try:
        test = Player.objects.create(name= name, user= user, clss='Barbarian',
        vit= c[0], str= c[1], agility= c[2],dex= c[3], inte= c[4], wis=c[5],
        pow= c[6], defen= c[7],hp= stats[0],
        max_hp= stats[0], mp= stats[1], max_mp= stats[1],speed= stats[2],
        dmg= stats[3], armor= stats[4], crit_chance= stats[5], armmor_pen= stats[6],
        regeneration= stats[7], mana_regeneration= stats[8], s_pow= stats[9],
        magic_pen= stats[10], magic_a= stats[11], dodge= stats[12]);
        #print(test + " udalo sie !")
        return "Success"
    elif clss == '3':
        c = set_random_perks(Mage);
        stats = get_stats_from_perks(c)

        #try:
        test = Player.objects.create(name= name, user= user, clss='Mage',
        vit= c[0], str= c[1], agility= c[2],dex= c[3], inte= c[4], wis=c[5],
        pow= c[6], defen= c[7],hp= stats[0],
        max_hp= stats[0], mp= stats[1], max_mp= stats[1],speed= stats[2],
        dmg= stats[3], armor= stats[4], crit_chance= stats[5], armmor_pen= stats[6],
        regeneration= stats[7], mana_regeneration= stats[8], s_pow= stats[9],
        magic_pen= stats[10], magic_a= stats[11], dodge= stats[12]);
        #print(test + " udalo sie !")
        return "Success"
    elif clss == '4':
        c = set_random_perks(Thief);
        stats = get_stats_from_perks(c)

        #try:
        test = Player.objects.create(name= name, user= user, clss='Thief',
        vit= c[0], str= c[1], agility= c[2],dex= c[3], inte= c[4], wis=c[5],
        pow= c[6], defen= c[7],hp= stats[0],
        max_hp= stats[0], mp= stats[1], max_mp= stats[1],speed= stats[2],
        dmg= stats[3], armor= stats[4], crit_chance= stats[5], armmor_pen= stats[6],
        regeneration= stats[7], mana_regeneration= stats[8], s_pow= stats[9],
        magic_pen= stats[10], magic_a= stats[11], dodge= stats[12]);
        #print(test + " udalo sie !")
        return "Success"
    elif clss == '5':
        c = set_random_perks(Monk);
        stats = get_stats_from_perks(c)

        #try:
        test = Player.objects.create(name= name, user= user, clss='Monk',
        vit= c[0], str= c[1], agility= c[2],dex= c[3], inte= c[4], wis=c[5],
        pow= c[6], defen= c[7],hp= stats[0],
        max_hp= stats[0], mp= stats[1], max_mp= stats[1],speed= stats[2],
        dmg= stats[3], armor= stats[4], crit_chance= stats[5], armmor_pen= stats[6],
        regeneration= stats[7], mana_regeneration= stats[8], s_pow= stats[9],
        magic_pen= stats[10], magic_a= stats[11], dodge= stats[12]);
        #print(test + " udalo sie !")
        return "Success"
