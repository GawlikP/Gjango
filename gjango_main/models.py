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
    name = models.CharField(max_length=100)
    hp = models.FloatField(default=0.0)
    max_hp = models.FloatField(default=0.0)
    mp = models.FloatField(default=0.0)
    max_mp = models.FloatField(default=0.0)
    speed = models.FloatField(default=0.0)
    dmg = models.FloatField(default=0.0)
    vit = models.FloatField(default=0.0)
    str = models.FloatField(default=0.0)
    agility = models.FloatField(default=0.0)
    dex = models.FloatField(default=0.0)
    inte = models.FloatField(default=0.0)
    wis = models.FloatField(default=0.0)
    pow = models.FloatField(default=0.0)
    # character = models.ForeignKey(Player,null=True, related_name='Player', on_delete=models.SET_NULL);
    user = models.ForeignKey(User,null=True, related_name='User', on_delete=models.CASCADE);
    def __str__(self):
        return self.name;
    class Meta:
        verbose_name_plural = 'Player'
