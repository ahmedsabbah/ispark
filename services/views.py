from django.shortcuts import render, redirect
from models import Opportunity, Tour, Conference
from applications.models import TourApplication
from contents.models import Contact
from django.utils import timezone

# Create your views here.
def major_exploration(request):
    tours = Tour.objects.filter(start_date__gte = timezone.now())
    addresses = Contact.objects.filter(type='AD')
    emails = Contact.objects.filter(type='EM')
    phones = Contact.objects.filter(type='PH')
    try:
        fb = Contact.objects.get(type='FB')
    except Contact.DoesNotExist:
        fb = ''
    try:
        tw = Contact.objects.get(type='TW')
    except Contact.DoesNotExist:
        tw = ''
    try:
        ins = Contact.objects.get(type='IN')
    except Contact.DoesNotExist:
        ins = ''
    try:
        yt = Contact.objects.get(type='YT')
    except Contact.DoesNotExist:
        yt = ''
    return render(request, 'major_exploration.html', {'tours': tours, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

def tour_apply(request, pk):
    try:
        tour = Tour.objects.get(pk=pk)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        school = request.POST.get('school', None)
        grade = request.POST.get('grade', None)
        wave = request.POST.get('wave', None)
        major1 = request.POST.get('major1', None)
        major2 = request.POST.get('major2', None)
        major3 = request.POST.get('major3', None)
        event_yes = request.POST.get('check3', None)
        event_no = request.POST.get('check4', None)
        event = request.POST.get('event', None)
        about_us = request.POST.get('about_us', None)

        application = TourApplication(tour=tour, name=name, email=email, phone=phone, school_name=school, grade_level=grade, wave=wave, know_about_us=about_us)
        if event_yes == '1':
            application.joined_previous_event=True
            application.previous_event=event
        else:
            application.joined_previous_event=False
        application.save()

        if major1:
            application.majors.add(major1)
        if major2 and major2 != major1:
            application.majors.add(major2)
        if major3 and major3 != major1 and major3 != major2:
            application.majors.add(major3)

        application.save()

        return redirect('/majors')
    except Tour.DoesNotExist:
        return redirect('/404')

def conferences(request):
    upcoming_conferences = Conference.objects.filter(start_date__gte = timezone.now())
    previous_conferences = Conference.objects.filter(start_date__lt = timezone.now())
    addresses = Contact.objects.filter(type='AD')
    emails = Contact.objects.filter(type='EM')
    phones = Contact.objects.filter(type='PH')
    try:
        fb = Contact.objects.get(type='FB')
    except Contact.DoesNotExist:
        fb = ''
    try:
        tw = Contact.objects.get(type='TW')
    except Contact.DoesNotExist:
        tw = ''
    try:
        ins = Contact.objects.get(type='IN')
    except Contact.DoesNotExist:
        ins = ''
    try:
        yt = Contact.objects.get(type='YT')
    except Contact.DoesNotExist:
        yt = ''
    return render(request, 'conferences.html', {'upcoming_conferences': upcoming_conferences, 'previous_conferences': previous_conferences, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

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
