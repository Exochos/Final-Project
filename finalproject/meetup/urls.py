from django.urls import path, include
from .views import *

# Various Urls we will be using for the website
urlpatterns=[
    path('', index, name='index'),
    
    
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]
