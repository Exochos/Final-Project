from django.urls import path, include
from .views import *
from meetup import views

# Various Urls we will be using for the website
urlpatterns=[
    path('', index, name='index'),

    path('login/', views.login, name='login'),
    
    
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    

]
