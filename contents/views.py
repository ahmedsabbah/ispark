from django.shortcuts import render, redirect
from models import Contact, TeamMember, Mentor, Category
from services.models import Vacancy
from applications.models import ContactForm, VacancyApplication

from django.core import serializers
from django.http.response import HttpResponse

def home(request):
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
    return render(request, 'home.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        number = request.POST.get('number', None)
        message = request.POST.get('message', None)
        if name and email and number and message:
            form = ContactForm(name=name, email=email, number=number, message=message)
            form.save()
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
