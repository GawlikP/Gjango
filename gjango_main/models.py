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
    hp = models.FloatField()
    max_hp = models.FloatField()
    mp = models.FloatField()
    max_mp = models.FloatField()
    speed = models.FloatField()
    dmg = models.FloatField()
    # character = models.ForeignKey(Player,null=True, related_name='Player', on_delete=models.SET_NULL);
    user = models.ForeignKey(User,null=True, related_name='User', on_delete=models.CASCADE);
    def __str__(self):
        return self.name;
    class Meta:
        verbose_name_plural = 'Player'
