from django.shortcuts import render, redirect
from models import Contact, TeamMember, Mentor, Category, Job, SliderSecondary, Testimonial, Partner
from services.models import Vacancy, Conference, Tour
from applications.models import VacancyApplication
from django.utils import timezone

from django.core import serializers
from django.http.response import HttpResponse

def home(request):
    second_sliders = SliderSecondary.objects.all()
    testimonials = Testimonial.objects.all()
    all_conferences = Conference.objects.all()
    all_tours = Tour.objects.all()
    tours = all_tours.filter(start_date__gte = timezone.now()).order_by('start_date')
    tours_to_show = tours[:2]
    conferences = all_conferences.filter(start_date__gte = timezone.now()).order_by('start_date')
    if tours_to_show.count() == 0:
        conferences_to_show = conferences[:3]
    else:
        if tours_to_show.count() == 1:
            conferences_to_show = conferences[:2]
        else:
            conferences_to_show = conferences[:1]
    partners_schools = Partner.objects.filter(type='S')
    partners_universities = Partner.objects.filter(type='U')
    partners_companies = Partner.objects.filter(type='C')
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
    return render(request, 'home.html', {'partners_schools': partners_schools,'partners_universities': partners_universities,'partners_companies': partners_companies,'tours_to_show': tours_to_show, 'conferences_to_show': conferences_to_show, 'tours': all_tours, 'conferences': all_conferences, 'testimonials': testimonials,'second_sliders': second_sliders, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

def jobs_majors(request):
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
    return render(request, 'jobs_majors.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

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

def mentors(request):
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
            mentors = Mentor.objects.filter(areas_of_expertise=category)
            data = serializers.serialize("json", mentors)
            return HttpResponse(data, content_type='application/json')
        except Category.DoesNotExist:
            category = Category.objects.first()
            categories = Category.objects.all()
            mentors = Mentor.objects.filter(areas_of_expertise=category)
            return render(request, 'mentors.html', {'categories': categories, 'emails': emails, 'addresses': addresses, 'phones': phones, 'mentors': mentors, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
    else:
        category = Category.objects.first()
        categories = Category.objects.all()
        mentors = Mentor.objects.filter(areas_of_expertise=category)
        return render(request, 'mentors.html', {'categories': categories, 'emails': emails, 'addresses': addresses, 'phones': phones, 'mentors': mentors, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

def team_apply(request, pk):
    try:
        vacancy = Vacancy.objects.get(pk=pk)
        name = request.POST.get('name', None)
        age = request.POST.get('age', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email_address', None)
        university = request.POST.get('university', None)
        major = request.POST.get('major', None)
        year_of_study_graduation = request.POST.get('year_study', None)
        why_join = request.POST.get('why_join', None)
        experience = request.POST.get('experience', None)

        application = VacancyApplication(vacancy=vacancy, name=name, age=age, email=email, phone=phone, university=university, major=major, year_of_study_graduation=year_of_study_graduation, why_join=why_join, experience=experience)

        application.save()

        return redirect('/team')
    except Vacancy.DoesNotExist:
        return redirect('/404')

def team(request):
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
    cores = TeamMember.objects.filter(role='C')
    interns = TeamMember.objects.filter(role='I')
    job_vacancies = Vacancy.objects.filter(role='J')
    internship_vacancies = Vacancy.objects.filter(role='I')
    return render(request, 'team.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'cores': cores, 'interns': interns, 'job_vacancies': job_vacancies, 'internship_vacancies': internship_vacancies, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        number = request.POST.get('number', None)
        message = request.POST.get('message', None)
        if name and email and number and message:
            send_mail(
                'iSpark Contact Request',
                'Name: '+name+'\n'+'Email: '+email+'\n'+'Phone: '+number+'\n'+'Message:\n'+message,
                'ahmedsabba7@gmail.com',
                ['ahmedsabba7@gmail.com'],
                fail_silently=False,
            )
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
    phones_students = Contact.objects.filter(type='PP')
    phones_schools = Contact.objects.filter(type='PS')
    phones_universities = Contact.objects.filter(type='PU')
    phones_companies = Contact.objects.filter(type='PC')
    try:
        latitude = Contact.objects.get(type='LT')
        longitude = Contact.objects.get(type='LG')
    except Contact.DoesNotExist:
        latitude = 30.0444
        longitude = 31.2357
    return render(request, 'contact.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'latitude': latitude, 'longitude': longitude, 'phones_students': phones_students, 'phones_schools': phones_schools, 'phones_universities': phones_universities, 'phones_companies': phones_companies, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
