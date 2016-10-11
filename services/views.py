from django.shortcuts import render, redirect
from models import Opportunity, Tour, Conference
from applications.models import TourApplication, ConferenceApplication, OpportunityApplication
from contents.models import Contact, Category, Announcement
from django.utils import timezone

from django.core import serializers
from django.http.response import HttpResponse
from django.core.paginator import Paginator

import json

def major_exploration(request):
    tours = Tour.objects.filter(start_date__gte = timezone.now()).order_by('start_date')
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

def get_majors(request):
    tour_id = request.GET.get('tour', None)
    major1_id = request.GET.get('major1', None)
    major2_id = request.GET.get('major2', None)
    if tour_id and major1_id and major2_id:
        try:
            tour = Tour.objects.get(id=tour_id)
            majors = tour.majors.filter().exclude(id__in=[major1_id, major2_id])
            data = serializers.serialize("json", majors)
            return HttpResponse(data, content_type='application/json')

        except Tour.DoesNotExist:
            context = {
                'status': '404', 'reason': 'tour not found'
            }
            response = HttpResponse(context, content-type='application/json')
            response.status_code = 400
            return response
    elif tour_id and major1_id:
        try:
            tour = Tour.objects.get(id=tour_id)
            majors = tour.majors.all().exclude(id__in=[major1_id])
            data = serializers.serialize("json", majors)
            return HttpResponse(data, content_type='application/json')

        except Tour.DoesNotExist:
            context = {
                'status': '404', 'reason': 'tour not found'
            }
            response = HttpResponse(context, content-type='application/json')
            response.status_code = 400
            return response
    else:
        context = {
            'status': '400', 'reason': 'missing input'
        }
        response = HttpResponse(context, content-type='application/json')
        response.status_code = 400
        return response


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
    upcoming_conferences = Conference.objects.filter(start_date__gte = timezone.now()).order_by('start_date')
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
    if not request.user.is_authenticated() or request.user.is_superuser or request.user.is_staff:
        return redirect('/login')
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
    announcements = Announcement.objects.all().order_by('-created_date')[:5]
    return render(request, 'profile.html', {'announcements': announcements, 'tours': tours, 'conferences': conferences, 'profile': profile, 'badges': badges,'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})


def internships(request):
    if not request.user.is_authenticated() or request.user.is_superuser or request.user.is_staff:
        return redirect('/login')
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
    if not request.user.is_authenticated() or request.user.is_superuser or request.user.is_staff:
        return redirect('/login')
    try:
        internship = Opportunity.objects.get(pk=pk)
        requirements = internship.requirements.all()
        category = internship.industry
        related_tmp = Opportunity.objects.filter(industry=category).filter(start_date__gte = timezone.now())
        p = Paginator(related_tmp, 8)
        page = p.page(1)
        related = page.object_list
        try:
            applied_tmp = OpportunityApplication.objects.get(user=request.user.profile, opportunity=internship)
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


def internship_apply(request, pk):
    try:
        internship = Opportunity.objects.get(pk=pk)
        try:
            applied_tmp = OpportunityApplication.objects.get(user=request.user.profile, opportunity=internship)
        except OpportunityApplication.DoesNotExist:
            application = OpportunityApplication(user=request.user.profile, opportunity=internship)
            application.save()
        return HttpResponse('')
    except Opportunity.DoesNotExist:
        return redirect('/404')
