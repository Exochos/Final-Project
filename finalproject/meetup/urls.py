from django.urls import path, include
from .views import *
from meetup import views

# Various Urls we will be using for the website
urlpatterns=[
    path('', index, name='index'),

    path('login/', views.login, name='login'),
    path('getmeetup/', views.getmeetup, name='meetup'),
    path('getactivity/', views.getactivity, name='activity'),
    path('meetupdetail/<int:id>',views.meetupdetail, name='meetupdetail'),
    path('newmeetup/', views.newmeetup, name='newmeetup'),
    path('newactivity/', views.newactivity, name='newactivity'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),   

]
