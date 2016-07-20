from django.shortcuts import render, redirect
from models import Contact, TeamMember, Mentor
from services.models import Vacancy

# Create your views here.
def home(request):
    addresses = Contact.objects.filter(type='A')
    emails = Contact.objects.filter(type='E')
    phones = Contact.objects.filter(type='P')
    return render(request, 'home.html', {'emails': emails, 'addresses': addresses, 'phones': phones})

def jobs_majors(request):
    addresses = Contact.objects.filter(type='A')
    emails = Contact.objects.filter(type='E')
    phones = Contact.objects.filter(type='P')
    return render(request, 'jobs_majors.html', {'emails': emails, 'addresses': addresses, 'phones': phones})

def mentors(request):
    addresses = Contact.objects.filter(type='A')
    emails = Contact.objects.filter(type='E')
    phones = Contact.objects.filter(type='P')
    mentors = Mentor.objects.all()
    return render(request, 'mentors.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'mentors': mentors})

def team(request):
    addresses = Contact.objects.filter(type='A')
    emails = Contact.objects.filter(type='E')
    phones = Contact.objects.filter(type='P')
    cores = TeamMember.objects.filter(role='C')
    interns = TeamMember.objects.filter(role='I')
    job_vacancies = Vacancy.objects.filter(role='J')
    internship_vacancies = Vacancy.objects.filter(role='I')
    return render(request, 'team.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'cores': cores, 'interns': interns, 'job_vacancies': job_vacancies, 'internship_vacancies': internship_vacancies})

def contact(request):
    addresses = Contact.objects.filter(type='A')
    emails = Contact.objects.filter(type='E')
    phones = Contact.objects.filter(type='P')
    try:
        latitude = Contact.objects.get(type='D')
        longitude = Contact.objects.get(type='G')
    except Contact.DoesNotExist:
        latitude = 30.0444
        longitude = 31.2357
    return render(request, 'contact.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'latitude': latitude, 'longitude': longitude})
