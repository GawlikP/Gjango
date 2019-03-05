from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password

from django.db.models import Q
# Create your views here

from .forms import LoginForm
from .forms import RegisterForm
from .forms import CreatePlayerForm

from .models import User
from .models import Player
from .models import Battle


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
    err = None

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
                    err = 'Character already exist'
                if error:
                    print(error);
            else:
                err = 'Something goes wrong'
    else:
        form = CreatePlayerForm()

    context = {
        'error': err,
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
    characters = None
    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        user = request.COOKIES['username']
        loged_in = True

    if loged_in:
        ussr = User.objects.get(username= user);
        characters = Player.objects.all().filter(user= ussr);



    context = {
        'characters': characters,
        'navi_three': 'active',
        'is_logged': loged_in,
        'title': 'Game Lobby'
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

    if character:
        character.skill_points += Check_if_levelup(character);


    context = {
    'title': 'Character',
    'is_logged': loged_in,
    'character': character
    }

    return render(response, 'character.html', context);

def combat_game(response):
    character_name = None
    enemy = None
    battle =  None

    if 'username' in response.COOKIES and 'password' in response.COOKIES:
        user = response.COOKIES['username'];
        loged_in = True
    else: loged_in = False


    if response.POST:
        character_name = response.POST.get('characterSelect', '')
    else: return HttpResponse('Something goes wrong ;-; ');

    if character_name != None:
        character = Player.objects.get(name= character_name);
        lv = character.lv;
        ch_user = character.user;
        enemy = Player.objects.all().filter(~Q(user= ch_user),lv=lv);
        enemy_id = random.randint(1,len(enemy))
        if enemy_id and enemy:

            battle = Battle.objects.create(player_id= character.id, enemy_id= enemy[enemy_id-1].id);

    context = {
        'enemy': enemy[enemy_id-1],
        'player': character,
        'logged_in': loged_in,
        'title':'Combat Game'
    }
    request = render(response,'combat_game.html', context);

    if battle != None:
        request.set_cookie('battle_id',battle.id);
        print('battle id setted')
        request.set_cookie('character_id',character.id);
        print('character id setted')

    return request

def battle_finish(request):

    user = None
    battle_id = -1
    character_id = -1
    result = 'Error'
    logged_in = False
    exp_before = 0
    exp_now = 0

    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        user = request.COOKIES['username'];
        logged_in = True;
    if 'battle_id' in request.COOKIES and 'character_id' in request.COOKIES:
        battle_id = request.COOKIES['battle_id']
        character_id = request.COOKIES['character_id']


    if request.POST:
        battle_result = request.POST.get('battle_result', '')
        print(battle_result)
        print(battle_id)
        if battle_result == 'Victory' and battle_id != -1:
            m = Battle.objects.get(id=battle_id)
            m.result = True;
            m.save();
            result = 'Victory !!!';
            print(character_id)
            if character_id != -1:
                m = Player.objects.get(id=character_id);
                print("getting character id")
                exp_before = m.exp
                m.exp += 10 +(m.exp*0.5);
                exp_now = m.exp
                m.save();

        elif battle_result == 'Fail' and battle_id != -1:
            m = Battle.objects.get(id=battle_id)
            m.result = False;
            m.save();
            result = 'Fail'
        else:
            return HttpResponse('Error XD')
    Battle.objects.filter(~Q(id=battle_id),result= None).delete();

    context = {
        'exp_before': exp_before,
        'exp_now': exp_now,
        'result': result,
        'is_logged': logged_in,
        'title': 'Combat Result!'
    }

    response = render(request,'battle_finish.html',context)
    response.delete_cookie('battle_id')
    response.delete_cookie('character_id')
    return response;

def delete_character(request,id):

    user = None
    logged_in = False;

    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        user = request.COOKIES['username'];
        logged_in = True;
    if Player.objects.filter(id= id).exists():
        Player.objects.filter(id= id).delete();
    else:
        return HttpResponse("Character doesnt exist")

    context = {
        'logged_in': logged_in,
        'title' :'Character Deleted'
    }

    return render(request, 'delete_character.html', context)

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
