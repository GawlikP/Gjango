from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=600)
    def __str__(self):
        return self.username;
    class Meta:
        verbose_name_plural = 'User'

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    clss = models.CharField(max_length=30, default="Error");
    hp = models.FloatField(default=0.0)
    max_hp = models.FloatField(default=0.0)
    mp = models.FloatField(default=0.0)
    max_mp = models.FloatField(default=0.0)
    speed = models.FloatField(default=0.0)
    dmg = models.FloatField(default=0.0)
    armor = models.FloatField(default=0.0)
    crit_chance = models.FloatField(default=0.0)
    armmor_pen = models.FloatField(default=0.0)
    regeneration = models.FloatField(default=0.0)
    mana_regeneration = models.FloatField(default=0.0)
    s_pow = models.FloatField(default=0.0)
    magic_pen = models.FloatField(default=0.0)
    magic_a = models.FloatField(default=0.0)
    dodge = models.FloatField(default=0.0)
    vit = models.FloatField(default=0.0)
    str = models.FloatField(default=0.0)
    agility = models.FloatField(default=0.0)
    dex = models.FloatField(default=0.0)
    inte = models.FloatField(default=0.0)
    wis = models.FloatField(default=0.0)
    pow = models.FloatField(default=0.0)
    defen = models.FloatField(default=0.0)
    lv = models.IntegerField(default=1)
    exp = models.FloatField(default=0.0)
    # character = models.ForeignKey(Player,null=True, related_name='Player', on_delete=models.SET_NULL);
    user = models.ForeignKey(User,null=True, related_name='User', on_delete=models.CASCADE);
    def __str__(self):
        return self.name;
    class Meta:
        verbose_name_plural = 'Player'

class Battle(models.Model):
    player_id = models.IntegerField(default=-1);
    enemy_id = models.IntegerField(default=-1);
    result = models.BooleanField(null=True);

    def __str__(self):
        return str(self.id);
    class Meta:
        verbose_name_plural = 'Battle'
