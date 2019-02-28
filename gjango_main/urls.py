from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^loging_in/',views.login,name='login'),
    url(r'^register/',views.registration,name='registration'),
    url(r'^log_out/',views.logout,name='logout'),
    url(r'^game/', views.game,name="game"),
]
