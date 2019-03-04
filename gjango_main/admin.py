from django.contrib import admin

# Register your models here.

from .models import User
from .models import Player
from .models import Battle

admin.site.register(User)
admin.site.register(Player)
admin.site.register(Battle)
