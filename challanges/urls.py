from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.challenge_list, name='challenge_list'),
    url(r'^main.html$' , views.main, name='main'),
    url(r'^challenge/(?P<pk>\d+)/$', views.challenge_detail, name="challenge_detail"),
    url(r'^challenge/new/$', views.new_challenge, name='new_challenge'),
    url(r'^challenge/(?P<pk>\d+)/edit/$', views.edit_challenge, name='edit_challenge'),
    url(r'^challenge/complete/$', views.complete_challenge, name="complete_challenges"),
    url(r'^story_list/$', views.story_list, name='story_list'),


]

