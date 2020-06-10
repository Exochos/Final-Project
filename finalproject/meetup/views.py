from django.shortcuts import render

# Starting with the indexrender
def index(request):
    return render(request, 'meetup/index.html')

def home(request):
    return render(request, 'base.html')