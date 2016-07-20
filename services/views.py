from django.shortcuts import render, redirect
from models import Opportunity, Tour, Conference
from contents.models import Contact
from django.utils import timezone

# Create your views here.
def major_exploration(request):
    tours = Tour.objects.filter(start_date__gte = timezone.now())
    addresses = Contact.objects.filter(type='A')
    emails = Contact.objects.filter(type='E')
    phones = Contact.objects.filter(type='P')
    return render(request, 'major_exploration.html', {'tours': tours, 'emails': emails, 'addresses': addresses, 'phones': phones})

def conferences(request):
    upcoming_conferences = Conference.objects.filter(start_date__gte = timezone.now())
    previous_conferences = Conference.objects.filter(start_date__lt = timezone.now())
    addresses = Contact.objects.filter(type='A')
    emails = Contact.objects.filter(type='E')
    phones = Contact.objects.filter(type='P')
    return render(request, 'conferences.html', {'upcoming_conferences': upcoming_conferences, 'previous_conferences': previous_conferences, 'emails': emails, 'addresses': addresses, 'phones': phones})

def profile(request):
    return render(request, 'profile.html')

def jobs(request):
    return render(request, 'jobs.html')

def job(request, pk):
    try:
        job = Opportunity.objects.get(pk=pk)
        return render(request, 'job.html', {'job': job})
    except Opportunity.DoesNotExist:
        return redirect('/404')

def internships(request):
    return render(request, 'internships.html')

def internship(request, pk):
    return render(request, 'internship.html')
