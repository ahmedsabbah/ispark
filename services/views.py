from django.shortcuts import render, redirect
from models import Opportunity, Tour, Conference, Job
from applications.models import TourApplication, ConferenceApplication, OpportunityApplication
from contents.models import Contact, Category, Announcement
from django.utils import timezone

from django.core import serializers
from django.http.response import HttpResponse
from django.core.paginator import Paginator


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
    previous_conferences_tmp = Conference.objects.filter(start_date__lt = timezone.now())
    p = Paginator(previous_conferences_tmp, 5)
    page = p.page(1)
    previous_conferences = page.object_list
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

def conference_apply(request, pk):
    try:
        conference = Conference.objects.get(pk=pk)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        school = request.POST.get('school', None)
        grade = request.POST.get('grade', None)
        wave = request.POST.get('wave', None)
        payment = request.POST.get('check1', None)
        event_yes = request.POST.get('check3', None)
        event = request.POST.get('event', None)
        about_us = request.POST.get('about_us', None)

        application = ConferenceApplication(conference=conference, name=name, email=email, phone=phone, school_name=school, grade_level=grade, wave=wave, payment=payment, know_about_us=about_us)
        if event_yes == '1':
            application.joined_previous_event=True
            application.previous_event=event
        else:
            application.joined_previous_event=False
        application.save()

        return redirect('/conferences')
    except Conference.DoesNotExist:
        return redirect('/404')

def profile(request):
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

    profile = request.user.profile
    badges = profile.badges.all()
    tours = Tour.objects.all()
    conferences = Conference.objects.all()
    announcement = Announcement.objects.all().order_by('-created_date').first()
    return render(request, 'profile.html', {'announcement': announcement, 'tours': tours, 'conferences': conferences, 'profile': profile, 'badges': badges,'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})


def internships(request):
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

    internships_to_date = Opportunity.objects.filter(start_date__gte = timezone.now()).order_by('-start_date')
    query = request.GET.get('q', None)
    if query:
        try:
            category = Category.objects.get(id=query)
            internships_tmp = internships_to_date.filter(industry=category)
            p = Paginator(internships_tmp, 16)
            page = request.GET.get('p', 1)
            page = p.page(page)
            internships = page.object_list
            has_next = page.has_next()
            data = serializers.serialize("json", internships)
            return HttpResponse(data, content_type='application/json')
        except Category.DoesNotExist:
            category = Category.objects.first()
            categories = Category.objects.all()
            internships_tmp = internships_to_date.filter(industry=category)
            p = Paginator(internships_tmp, 16)
            page = p.page(1)
            internships = page.object_list
            has_next = page.has_next()
            return render(request, 'internships.html', {'internships': internships, 'has_next': has_next, 'categories': categories, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
    else:
        category = Category.objects.first()
        categories = Category.objects.all()
        internships_tmp = internships_to_date.filter(industry=category)
        p = Paginator(internships_tmp, 16)
        page = p.page(1)
        internships = page.object_list
        has_next = page.has_next()
        return render(request, 'internships.html', {'internships': internships, 'has_next': has_next, 'categories': categories, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

def internship(request, pk):
    try:
        internship = Opportunity.objects.get(pk=pk)
        requirements = internship.requirements.all()
        category = internship.industry
        related_tmp = Opportunity.objects.filter(industry=category)
        p = Paginator(related_tmp, 8)
        page = p.page(1)
        related = page.object_list
        try:
            applied_tmp = OpportunityApplication.objects.get(user=request.user, opportunity=internship)
            applied = True
        except OpportunityApplication.DoesNotExist:
            applied = False
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
        return render(request, 'internship.html', {'applied': applied, 'internship': internship, 'requirements': requirements, 'related': related, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
    except Opportunity.DoesNotExist:
        return redirect('/404')

def jobs(request):
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

    query = request.GET.get('q', None)
    if query:
        try:
            category = Category.objects.get(id=query)
            jobs = Job.objects.filter(category=category)
            data = serializers.serialize("json", jobs)
            return HttpResponse(data, content_type='application/json')
        except Category.DoesNotExist:
            category = Category.objects.first()
            categories = Category.objects.all()
            jobs = Job.objects.filter(category=category)
            return render(request, 'jobs.html', {'jobs': jobs, 'categories': categories, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
    else:
        category = Category.objects.first()
        categories = Category.objects.all()
        jobs = Job.objects.filter(category=category)
        return render(request, 'jobs.html', {'jobs': jobs, 'categories': categories, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

def job(request, pk):
    try:
        job = Job.objects.get(pk=pk)
        interests = job.interests.all()
        skills = job.skills.all()
        related = Job.objects.filter(category=job.category)
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
        return render(request, 'job.html', {'job': job, 'interests': interests, 'skills': skills, 'related': related, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
    except Job.DoesNotExist:
        return redirect('/404')

def internship_apply(request, pk):
    try:
        internship = Opportunity.objects.get(pk=pk)
        try:
            applied_tmp = OpportunityApplication.objects.get(user=request.user, opportunity=internship)
        except OpportunityApplication.DoesNotExist:
            application = OpportunityApplication(user=request.user, opportunity=internship)
            application.save()
        return HttpResponse('')
    except Opportunity.DoesNotExist:
        return redirect('/404')
