from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def jobs_majors(request):
    return render(request, 'jobs_majors.html')

def mentors(request):
    return render(request, 'mentors.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')
