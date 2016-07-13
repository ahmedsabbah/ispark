from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def jobs_majors(request):
    return render(request, 'jobs_majors.html')
