from django.urls import path, include
from .views import *

# Various Urls we will be using for the website
urlpatterns=[
    path('', index, name='index'),

]