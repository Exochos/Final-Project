from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import MeetUp, Activity

# Starting with the indexrender
def index(request):
    return render(request, 'meetup/index.html')

def home(request):
    return render(request, 'base.html')

def start(request):
    return render(request, 'start.html')

def getmeetup(request):
    meetup_list=MeetUp.objects.all()
    return render (request, 'meetup/meetup.html',{'meetup_list': meetup_list,})

def getactivity(request):
    activity_list=Activity.objects.all()
    return render (request, 'meetup/activity.html',{'activity_list': activity_list,})




def login(request):
    return render(request, 'registration/login.html')

def loginmessage(request):
    return render(request, 'meetup/loginmessage.html')

def logoutmessage(request):
    return render(request, 'meetup/logoutmessage.html')
