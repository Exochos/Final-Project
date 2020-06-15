from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MeetUp, Activity
from .forms import MeetUpForm, ActivityForm

# Starting with the indexrender
def index(request):
    return render(request, 'meetup/index.html')

# Grab the meetup
def getmeetup(request):
    meetup_list=MeetUp.objects.all()
    return render (request, 'meetup/meetup.html',{'meetup_list': meetup_list,})

# Grab the activity
def getactivity(request):
    activity_list=Activity.objects.all()
    return render (request, 'meetup/activity.html',{'activity_list': activity_list,})

# Meetup details form
def meetupdetails(request,id):
    obj = get_object_or_404(MeetUp, pk=id)
    context = {
        "object": obj
    }
    return render(request, "meetup/meetupdetail.html", context)


# new meetup form with login
@login_required
def newmeetup(request):
    form=MeetUpForm
    if request.method=='POST':
        form=MeetUpForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetUpForm
        else:
            form=MeetUpForm()
    return render(request, 'meetup/newmeetup.html', {'form': form})

# Activity login form required
@login_required
def newactivity(request):
    form=ActivityForm
    if request.method=='POST':
        form=ActivityForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ActivityForm()
        else:
            form=ActivityForm()
    return render(request, 'meetup/newactivity.html', {'form': form})


def login(request):
    return render(request, 'registration/login.html')

def loginmessage(request):
    return render(request, 'meetup/loginmessage.html')

def logoutmessage(request):
    return render(request, 'meetup/logoutmessage.html')
