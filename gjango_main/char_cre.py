import random
#points 16 + rand 4.0

Warrior = {
    'vit': 2.0,
    'str': 3.0,
    'agility': 1.5,
    'dex': 2.0,
    'inte': 2.0,
    'wis': 1.0,
    'pow':2.5,
    'def': 2.0,
}
Barbarian = {
    'vit': 5.0,
    'str': 2.0,
    'agility': 1.0,
    'dex': 1.5,
    'inte': 1.0,
    'wis': 1.0,
    'pow':2.0,
    'def':2.5,
}

Mage = {
    'vit': 1.0,
    'str': 1.0,
    'agility': 2.0,
    'dex': 1.0,
    'inte': 4.0,
    'wis': 3.0,
    'pow': 3.0,
    'def': 1.0,
}

Thief = {
    'vit': 1.5,
    'str': 2.0,
    'agility': 5.0,
    'dex': 3.0,
    'inte': 1.0,
    'wis': 1.5,
    'pow': 1.0,
    'def': 1.0,
}

Monk = {
    'vit': 2.0,
    'str': 2.0,
    'agility': 1.0,
    'dex': 6.0,
    'inte': 1.0,
    'wis': 1.0,
    'pow': 1.0,
    'def': 2.0,

}

def get_stats_from_perks(clss):

    hp = clss[0] * 10 + clss[1] + clss[7];                                          #
    mp = clss[0] + clss[3] + clss[4] * 5
    speed = clss[2] * 2
    dmg = clss[1] * 2 + clss[3] * 0.5 + clss[6]
    armor = clss[3] * 1.5  + clss[7]
    crit_chance = clss[2] * 0.5
    armor_pen = clss[2] * 0.5 + clss[3] + clss[6] * 0.1
    regeneration = clss[0] * 2 + clss[1] * 0.5 + clss[7] * 0.1 + clss[7] * 0.5
    mana_regeneration = clss[0] + clss[4] * 3 + clss[6] * 0.5
    dodge = clss[2] * 2
    s_pow = clss[3] + clss[4] * 2 + clss[5] * 3 + clss[6] * 5
    magic_pen = clss[3] * 0.5  + clss[5] + clss[6] * 0.5
    magic_a = clss[0] * 0.5 + clss[3] + clss[4] + clss[7]

    return  hp,mp,speed,dmg,armor,crit_chance,armor_pen,regeneration,mana_regeneration,s_pow, magic_pen, magic_a, dodge;

def set_random_perks(clss):
    #random.randint(1,101)
    points = 4.0
    if points > 0.1: rnd = random.randint(1,int(points*100))/100
    else: rnd = 0.0;
    print(rnd);
    points -= rnd;
    vit = clss['vit'] + rnd;
    if points > 0.1: rnd = random.randint(1,int(points*100))/100
    else: rnd = 0.0;
    print(rnd);
    points -= rnd;
    str = clss['str'] + rnd;
    if points > 0.1: rnd = random.randint(1,int(points*100))/100
    else: rnd = 0.0;
    print(rnd);
    points -= rnd;
    agility = clss['agility'] + rnd
    if points > 0.1: rnd = random.randint(1,int(points*100))/100
    else: rnd = 0.0;
    print(rnd);
    points -= rnd;
    dex = clss['dex'] + rnd
    if points > 0.1: rnd = random.randint(1,int(points*100))/100
    else: rnd = 0.0;
    print(rnd);
    points -= rnd;
    inte = clss['inte'] + rnd
    if points > 0.1: rnd = random.randint(1,int(points*100))/100
    else: rnd = 0.0;
    print(rnd);
    points -= rnd;
    wis = clss['wis'] + rnd
    if points > 0.1: rnd = random.randint(1,int(points*100))/100
    else: rnd = 0.0;
    print(rnd);
    points -= rnd;
    pow = clss['pow'] + rnd
    if points > 0.1: rnd = random.randint(1,int(points*100))/100
    else: rnd = 0.0;
    print(rnd);
    points -= rnd;
    defen = clss['def'] + rnd
        #    1,  2 , 3    ,  4, 5  , 6, 7,   8
    return vit,str,agility,dex,inte,wis,pow,defen;
