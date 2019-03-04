from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^loging_in/',views.login,name='login'),
    url(r'^register/',views.registration,name='registration'),
    url(r'^log_out/',views.logout,name='logout'),
    url(r'^game/', views.game,name="game"),
    url(r'^character/(?P<id>\d+)/$',views.character, name='character'),
    url(r'^combat_game/',views.combat_game, name='combat_game'),
    url(r'^battle_finish/',views.battle_finish, name='battle_finish'),
    url(r'^delete_character/(?P<id>\d+)/$',views.delete_character, name='delete_character'),
    #r'^(?P<id>\d+)/$'
]
